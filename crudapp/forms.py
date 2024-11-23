from django import forms
from .models import *


class AddFruitForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = ['name', 'price']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'fruit name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }