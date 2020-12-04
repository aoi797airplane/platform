from django import forms
from account.models import Profile
from .models import Ea

class EaForm(forms.ModelForm):

    ea = forms.ModelMultipleChoiceField(
        queryset=Ea.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:

        model = Profile
        fields = ['ea',]
        # widgets= {
        #     'gender': forms.RadioSelect
        # }
