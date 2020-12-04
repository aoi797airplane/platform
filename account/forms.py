from django import forms
from .models import Profile, User

class AccountForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ('account', 'username', 'kana_username', 'gender', 'age',)
        widgets= {
            'gender': forms.RadioSelect
        }

class UserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ('email',)
  