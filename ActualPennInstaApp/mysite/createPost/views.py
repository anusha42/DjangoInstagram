from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
# def createPost(*args, **kwargs):
    # return HttpResponse("<h2>Hello, world. You're at the create post.</h2>")

def createPost(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        
        instance = form.save(commit=False)
        instance.usernm = request.user
        instance.save() 
        form.save()       
        return redirect('/home/')

    context = {
        'form': form
    }
    return render (request, "createPostTemp.html", context)         

def post_view(request):
    allObj = Post.objects.all()
    # context = {
         # 'userid': allObj.usernm,
         # 'text': allObj.post_text
    # }
    print(allObj)
    return render(request, 'home.html', {'all':allObj})
    # return render(request, 'postView.html', context)