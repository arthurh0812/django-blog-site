from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'webapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'webapp/userposts.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'webapp/detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'webapp/postcreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def message(self, request):
        messages.success(request, f"Your Post has been created")
        return redirect('/')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'webapp/postupdate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'webapp/postdelete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def About(request):
    return render(request, "webapp/about.html", {'title': 'About'})

