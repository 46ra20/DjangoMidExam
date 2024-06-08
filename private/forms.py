from public.models import ProductModel
from django import forms

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'