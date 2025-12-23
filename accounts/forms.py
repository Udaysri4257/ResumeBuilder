from django import forms
from django.core.validators import RegexValidator

class LogInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one number, and one special character."
            )
        ]
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )

