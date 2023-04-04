from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from random import sample
from .models import Post
from .forms import PostForm, UserFormRegistration
from django.views.generic import ListView, DetailView, DeleteView

from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden



def main_page(request):
    posts = list(Post.objects.all())
    random_posts = sample(posts, 3)
    data = {
            "posts": random_posts,
    }
    if request.user.is_anonymous:
        return render(request, 'blog/main_page_content.html', context=data)   
    else:
        username = request.user.username
        data |= {
            'username': username,
        }
        return render(request, 'blog/main_page_content.html', context=data)     


class AllPosts(ListView):
    template_name = 'blog/list_detail.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):   # тут как бы все хорошо но есть хуйня с несоблюдением принципа gry
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


class OnePost(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'
    

    def get_context_data(self, **kwargs):       # тут тоже, чат gpt предложил context processor использовать 
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        post = self.get_object()
        if self.request.user.id == post.author_id:  # но это отличие от аналогичного метода в AllPosts
            context |= {'is_author': 'is_author'}
        return context


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        return self.request.user.id == post.author_id


    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return HttpResponseForbidden('Редактировать этот пост может только автор')
        return super().dispatch(request, *args, **kwargs)


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        return self.request.user.id == post.author_id


    def handle_no_permission(self):
        return HttpResponseForbidden('Удалить этот пост может только автор')


class CreateUser(CreateView):
    model = User
    form_class = UserFormRegistration
    template_name = 'blog/registration.html'
    success_url = '/'

