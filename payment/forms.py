from django import forms
from.models import Payment
class PaymentUploadForm(forms.ModelForm):
    class Meta:
        model= Payments
        fields= "__all__"