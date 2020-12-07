from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class RegisterView(generic.CreateView):
    template_name = 'members/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
