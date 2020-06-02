from django.urls import path

from . import views

from . import createPost, post_view

urlpatterns = [
    path('/viewPosts', post_view, name='viewPosts'),
    path('/create', createPost, name='createPost'),
    
]