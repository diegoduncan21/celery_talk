from django import forms


class RegisterUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmation = forms.CharField(widget=forms.PasswordInput)
