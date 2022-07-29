from django.core import validators
from django import forms
#from matplotlib import widgets
from bts.models import AddBug


class BugRegistration(forms.ModelForm):
  class Meta:
      model=AddBug
      fields=['bugname','bugdate','bugpriority','projectname','content']
      widgets={
          #'bugdate':forms.DateInput(attrs={'class':'form-control'}),
      }



