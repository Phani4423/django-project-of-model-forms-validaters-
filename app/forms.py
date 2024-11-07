from app.models import *
from django import forms
class studentsforms(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'
    remail = forms.EmailField()
    botcatcher = forms.CharField(widget=forms.HiddenInput,required=False)
    def clean(self):
        fe = self.cleaned_data['email']
        se = self.cleaned_data['remail']
        if se != fe:
            raise forms.ValidationError('error')
    def clean_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('data is not entered by human')
        
        
