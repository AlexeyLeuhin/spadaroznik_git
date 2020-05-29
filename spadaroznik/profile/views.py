from django.shortcuts import render
from register.forms import SignUpForm
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .forms import ProfileRedactForm


def show_profile(request, pk):
    if not request.user.is_authenticated:
        form = SignUpForm()
        return render(request, 'login/login.html', context={'form': form})
    curr_us = get_object_or_404(User, id=pk)
    profile = Profile.objects.filter(user=curr_us)
    if request.user == curr_us:
        return render(request, 'profile/ur_profile.html', context={'profile': profile})
    else:
        return render(request, 'profile/not_ur_profile.html', context={'profile': profile})


class ProfileRedact(View):

    def get(self, request):
        if not request.user.is_authenticated:
            form = SignUpForm()
            return render(request, 'login/login.html', context={'form': form})

        form = ProfileRedactForm()
        return render(request, 'profile/ur_profile_redact.html', context={'form': form})

    def post(self, request):
        bound_form = ProfileRedactForm(request.POST, request.FILES)
        if bound_form.is_valid():
            user = request.user
            profile = Profile.objects.filter(user=user)
            bound_form.save(user)
            return render(request, 'profile/ur_profile.html', context={'profile': profile})
        return render(request, 'profile/ur_profile_redact.html', context={'form': bound_form})
