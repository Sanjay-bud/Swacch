from django import forms
from . import models

class userdetailsform(forms.ModelForm):
    class Meta:
        model = models.form
        fields = ['name', 'adr', 'phn_num', 'mem_count']

class phn_get(forms.ModelForm):
    class Meta:
        model= models.form_check
        fields = "__all__"

