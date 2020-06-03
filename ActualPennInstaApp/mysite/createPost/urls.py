from django.urls import path

from . import views

from . import createPost, post_view

urlpatterns = [
    path('/home', post_view, name='home'),
    path('/create', createPost, name='createPost'),
    
]