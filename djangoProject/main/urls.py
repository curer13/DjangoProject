from .views import *
from django.urls import path, include

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('create/', AddPostView.as_view(), name='create'),
    path('<int:pk>/post/', PostsDetailView.as_view(), name='article-detail'),
    path('edit/<int:pk>/', UpdatePostView.as_view(), name='edit-article'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete-article'),
]