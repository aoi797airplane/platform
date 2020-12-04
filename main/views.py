from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User, Profile
from .models import Ea
from .forms import EaForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def ea(request):
    ea = Ea.objects.all()
    return render(request, 'ea.html', {'ea': ea})

@login_required
def ea_request(request):
    try:
        user = request.user
        email = user
        profile = Profile.objects.get(user= user)
        ea = Ea.objects.all()
        try:
            account = profile.account
        except:
            error = '口座番号がまだ登録されていません'
            return render(request, 'request.html', {'error': error})

    except:
        error = 'このユーザーは存在しません'
        return render(request, 'request.html', {'error': error})
    

       
    if request.method == 'POST':
        ea = request.POST['ea']
        profile.ea.add(ea)

        profile.save()
        return redirect('home')

    form = EaForm(instance= profile)
    
    return render(request, 'request.html', {'account' : account, 'email': email, 'ea' : ea})



def termsofservice(request):
    return render(request, 'termsofservice.html')
    
def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def how_to_use(request):
    return render(request, 'how_to_use.html')