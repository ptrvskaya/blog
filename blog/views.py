from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, UpdateView
from random import sample
from .models import Post
from .forms import PostForm, UserFormRegistration
from django.views.generic import ListView, DetailView, DeleteView

from django.contrib.auth.models import User


def main_page(request):
    posts = list(Post.objects.all())
    random_posts = sample(posts, 3)
    data = {
        "posts": random_posts,
    }
    return render(request, 'blog/main_page_content.html', context=data)     


class AllPosts(ListView):
    template_name = 'blog/list_detail.html'
    model = Post
    context_object_name = 'posts'


class OnePost(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = '/'


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = '/'


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/'


class CreateUser(CreateView):
    model = User
    form_class = UserFormRegistration
    template_name = 'blog/registration.html'
    success_url = '/'