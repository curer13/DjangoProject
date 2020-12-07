from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['publisher', 'topic', 'text', 'date']

        '''widgets = {
            'publisher': TextInput(attrs={'class': 'form-control'}),
            'topic': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control'}),
            'date': DateTimeInput(attrs={'class': 'form-control'})
        }'''
