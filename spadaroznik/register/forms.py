from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=120, label='Логин')
    email = forms.CharField(label='Электронная почта')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль', error_messages={})
    password_verify = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    def clean_password_verify(self):
        password = self.cleaned_data['password']
        password_verify = self.cleaned_data['password_verify']
        if password != password_verify:
            raise forms.ValidationError(u'Пароли не совпадают.')
        elif len(password) < 8:
            raise forms.ValidationError(u'Пароль должен быть длиной не менее 8 символов.')
        else:
            return password_verify

    def clean_username(self):
        new_usname = self.cleaned_data['username']
        if User.objects.filter(username=new_usname).exists():
            raise forms.ValidationError(u'Имя пользователя "%s" уже используется.' % new_usname)
        else:
            return new_usname

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@'not in email:
            raise forms.ValidationError(u'Неверный email, поле должно содержать символ @')
        elif email.endswith('@'):
            raise forms.ValidationError(u'Адрес электронной почты неверный.')
        else:
            return email

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        email=self.cleaned_data['email'],
                                        password=self.cleaned_data['password'])
        user.save()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cd = self.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is None:
            raise forms.ValidationError(u'Неверное имя пользователя или пароль')
        return cd



