from django import forms
from .models import Complaint

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your shipping address'}))
    coupon = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter coupon code'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))



class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'subject', 'message']