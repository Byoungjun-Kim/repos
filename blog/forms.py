from django import forms
from .models import EnrollList

class EnrollForm(forms.ModelForm) :
    class Meta :
        model  = EnrollList
        fields = ('code', 'memo', 'prof', 'location', 'start', 'end', 'day', 'lecture_info')
