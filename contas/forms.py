from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            self.add_error('email', 'Este email já está em uso.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            if 'form-control' not in classes:
                field.widget.attrs['class'] = (classes + ' form-control').strip()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.strip()
            if '@' not in email:
                raise forms.ValidationError('O email deve conter o caractere "@".')
            return email.lower()
        return email
