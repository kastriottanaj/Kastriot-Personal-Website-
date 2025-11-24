from django import forms
from .models import NewsletterSignup

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        }