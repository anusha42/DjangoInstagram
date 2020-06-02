from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("instagram:homepage")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def create_request(request):
    createPost(request)
    messages.info(request, "Created successfully!")
    # return redirect("instagram:homepage")
