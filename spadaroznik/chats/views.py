from django.shortcuts import render


def chat_choose(request):
    return render(request, 'chats/chat_choose.html')

def room(request, room_name):
    return render(request, 'chats/room.html', {
        'room_name': room_name
    })
