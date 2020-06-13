from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignUpForm, LoginForm
from django.views.generic import View
from django.contrib.auth import authenticate, login as auth_login


class Register(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'sign_up/register.html', context={'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect(reverse("profile_redact_url"))
        return render(request, 'sign_up/register.html', context={'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


