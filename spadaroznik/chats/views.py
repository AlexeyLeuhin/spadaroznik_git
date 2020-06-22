from django.shortcuts import render
from .models import Chat


def chat_choose(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    return render(request, 'chats/chat_choose.html', context={'chats': chats})


def room(request, room_name):
    return render(request, 'chats/room.html', {
        'room_name': room_name
    })
