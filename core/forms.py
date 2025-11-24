from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Ihr Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Ihre E-Mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Nachricht', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))