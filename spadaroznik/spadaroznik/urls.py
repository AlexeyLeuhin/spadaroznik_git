from django.contrib import admin
from django.urls import path
from main_page import views as main_page_views
from register import views as register_views
from posts import views as posts_views
from profile import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_views.index),
    path('signup/', register_views.Register.as_view(), name="signUp_url"),
    path('login/', register_views.login, name="login_url"),
    path('posts/', posts_views.posts_list),
    path('posts/create', posts_views.PostCreate.as_view(), name='post_create_url'),
    path('posts/<int:pk>/', posts_views.PostDetail.as_view()),
    path('profile/<int:pk>/', profile_views.show_profile),
    path('profile/redact/', profile_views.ProfileRedact.as_view(), name="profile_redact_url"),
]
