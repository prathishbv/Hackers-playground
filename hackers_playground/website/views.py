from django.shortcuts import render, redirect
from .models import User
from django.forms import modelform_factory
from .form import RegisterForm
# Create your views here.
def welcome(request):
    return render(request, "website/home.html")

# RegisterForm = modelform_factory(User, exclude=[])
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = RegisterForm()      
    return render(request, "website/register.html", {"form": form})