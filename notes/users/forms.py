from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    first_name = forms.CharField(
        max_length=30, required=False, widget=forms.TextInput()
    )
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput())
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )
    location = forms.CharField(max_length=100, required=False, widget=forms.TextInput())
    bio = forms.CharField(required=False, widget=forms.Textarea())
    telephone = forms.CharField(max_length=15, required=False, widget=forms.TextInput())

    class Meta:
        model = Profile
        fields = [
            "avatar",
            "first_name",
            "last_name",
            "date_of_birth",
            "location",
            "bio",
            "telephone",
        ]

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        if telephone and not telephone.isdigit():
            raise ValidationError("Номер телефону повинен містити лише цифри.")
        return telephone
