from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chats.models import Chat, Message
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
    profile = get_object_or_404(Profile, user=curr_us)
    if request.user == curr_us:
        return render(request, 'profile/ur_profile.html', context={'profile': profile})
    else:
        return render(request, 'profile/not_ur_profile.html', context={'profile': profile, 'pk': pk})


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
            bound_form.save(user)
            profile = get_object_or_404(Profile, user=user)
            return render(request, 'profile/ur_profile.html', context={'profile': profile})
        return render(request, 'profile/ur_profile_redact.html', context={'form': bound_form})


@login_required(login_url='login_url')
def write_button_handler(request, pk):
    curr_us = get_object_or_404(User, id=pk)
    chat = Chat.objects.filter(members=curr_us).filter(members=request.user)
    messages = []
    if len(chat) > 0:
        chat = chat[0]
        messages = Message.objects.filter(chat=chat)
    else:
        chat = Chat()
        chat.save()
        chat.members.add(curr_us)
        chat.members.add(request.user)
        chat.save()
    return render(request, 'chats/room.html', context={'messages': messages, 'room_name': str(chat.id)})

