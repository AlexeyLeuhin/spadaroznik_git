from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_choose, name='chat_choose'),
    path('<str:room_name>/', views.room, name='room'),
]