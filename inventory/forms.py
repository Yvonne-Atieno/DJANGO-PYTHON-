from django import forms
from.models import Product
class ProductUploadForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= "_all_"