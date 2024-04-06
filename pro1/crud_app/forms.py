from .models import Grocery
from django import forms

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = "__all__"

