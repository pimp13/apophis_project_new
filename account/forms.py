from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(attrs={
            "class": "form-control border-0 bg-light rounded-end ps-1",
            "placeholder": "***@gmail.com"
        }),
        validators=[
            validators.EmailValidator,
        ]
    )
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            "class": "form-control border-0 bg-light rounded-end ps-1",
            "placeholder": "نام کاربری شما"
        }),
        validators=[
            validators.MinLengthValidator(5),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            "class": "form-control border-0 bg-light rounded-end ps-1",
            "placeholder": "*********"
        }),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            "class": "form-control border-0 bg-light rounded-end ps-1",
            "placeholder": "*********"
        }),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )
    site_rules = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        error_messages={
            'required': 'تیک قوانین سایت رو حتما باید تایید کنید'
        }
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه های عبور با یک دیگر یکسان نیستند')

class LoginForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "مثال: test"}),
        validators=[
            validators.MinLengthValidator(5),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "*********"}),
        validators=[
            validators.MinLengthValidator(8),
        ]
    )
