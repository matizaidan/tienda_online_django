from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
