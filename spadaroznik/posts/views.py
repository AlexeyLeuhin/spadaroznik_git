from django.shortcuts import render
from .models import Publications
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm
from register.forms import SignUpForm


def posts_list(request):
    posts = Publications.objects.all()
    return render(request, "posts/posts.html", context={'posts': posts})


# shows full post info after you click any post in post list
class PostDetail(View):

    def get(self, request, pk):
        post = get_object_or_404(Publications, pk=pk)
        return render(request, "posts/post.html", context={'post': post})


class PostCreate(View):

    def get(self, request):
        if not request.user.is_authenticated:
            form = SignUpForm()
            return render(request, 'login/login.html', context={'form': form})
        form = PostForm()
        return render(request, 'posts/create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            post = bound_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/posts")
        return render(request, 'posts/create.html', context={'form': bound_form})
