from django.shortcuts import render, redirect, get_object_or_404
from .models import Forum
from .forms import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def about(request):
    return render(request, 'main/about.html')


class PostsDetailView(DetailView):
    model = Forum
    template_name = 'main/article_detail.html'


class Home(ListView):
    model = Forum
    template_name = 'main/index.html'
    ordering = ['-date']


class AddPostView(CreateView):
    model = Forum
    form_class = ForumForm
    template_name = 'main/create.html'
    # fields = ('publisher', 'topic', 'text', 'date')

class UpdatePostView(UpdateView):
    model = Forum
    template_name = 'main/update.html'
    fields = '__all__'

class DeletePostView(DeleteView):
    model = Forum
    template_name = 'main/delete.html'
    success_url = reverse_lazy('home')


