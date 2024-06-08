from django import forms
from .models import Comments

class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields="__all__"