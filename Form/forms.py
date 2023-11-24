from django import forms
from django.forms import ModelForm
from .models import FQ

class FormQuestions(ModelForm):
    class Meta:
       model = FQ
       fields = ('name',
                'sexuality', 
                'neurodivergence', 
                'mbti', 
                'ethnicity', 
                'disability',
                'confort',
                'identity',
                'trans',
                'country')
