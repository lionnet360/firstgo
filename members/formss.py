from django import forms
from .models import Poost

class PostForm(forms.ModelForm):
    class Meta:
        model = Poost
        fields = ['title', 'content']

