from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from django.contrib import auth
from django.conf import settings
from .forms import AccountForm,UserForm


def signup(request):
    
    if request.method == 'POST':

        Email = request.POST['email']
        Password = request.POST['password']
           
        try:
            User.objects.get(email = Email)
            return render(request, 'signup.html', {'error': 'このメールは既に登録されています'})
        except:

            user = User.objects.create_user(email=Email, password=Password)
            user.save()
            profile = Profile.objects.create( user = user)
            profile.save()

        
            return redirect('login')
        
    return render(request, 'signup.html')



def Login(request):
    if request.method == 'POST':
        Password= request.POST['password']
        Email = request.POST['email']
        try:
            user = User.objects.get(email= Email)

            try:
                user = authenticate(request, email = Email, password = Password)
                login(request, user)
                profile = Profile.objects.get(user = request.user)
                profile.login_count = profile.login_count + 1
                profile.save()
                print(profile.login_count)

                return redirect('home')
            except:
                return render(request, 'login.html', {'error':'パスワードが違います' })
        except:
            return render(request, 'login.html', {'error':'このメールアドレスは存在しません' })
           
    return render (request, 'login.html')
        

@login_required
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def user_info(request):
    user = request.user
    login(request, user)
    profile=get_object_or_404(Profile, user = user)
    ea = profile.ea.all()
    
    # user = User.objects.get(user = user)

    # profile = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=profile)
        userform = UserForm(request.POST, instance = user )
        if userform.is_valid():

            if form.is_valid():
                account = form.save()
                account.save()
                email = userform.save()
                email.save()
                login(request, user)
                return redirect('home')
        else:
            error : 'このメールアドレスは無効です'
            return render(request, 'user_info.html',  {'form': form, 'ea': ea, 'user': userform, 'error': error})
            
            
    else:
        form = AccountForm(instance=profile)
        userform = UserForm( instance = user )

    return render(request, 'user_info.html',  {'form': form, 'ea': ea, 'user': userform})
    

