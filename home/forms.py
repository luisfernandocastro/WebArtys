from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','categoria','precio', 'descripcion','foto']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control mb-3',
                'placeholder':'Dale un buen nombre a tu producto',
                }),
            'categoria': forms.Select(attrs={'class':'form-select mb-3'}),
            'precio': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'descripcion': forms.Textarea(attrs={
                'class':'form-control mb-3',
                'placeholder': 'Describe tu producto',
                }),
            'foto': forms.FileInput(attrs={'class':'form-control mb-3'}),
        }