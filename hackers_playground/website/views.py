from django.shortcuts import render
from .models import User
from django.forms import modelform_factory
# Create your views here.
def welcome(request):
    return render(request, "website/home.html")

RegisterForm = modelform_factory(User, exclude=[])
def register(request):
    form = RegisterForm()
    return render(request, "website/register.html", {"form": form})