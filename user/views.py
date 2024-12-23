from django.shortcuts import render, redirect, HttpResponse
from user.forms import Registerform, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
    if request.method == "GET":
        form = Registerform
        return render(request, "user/register.html", context={"form":form})
    if request.method == "POST":
        form = Registerform(request.POST)
        if not form.is_valid():
            return render(request, "user/register.html", context={"form":form})
        elif form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            User.objects.create_user(username=username, password=password)
            return redirect("/")
        
def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "user/login.html", context={"form":form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "user/login.html", context={"form":form})
        elif form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            if not user:
                form.add_error("username", "Invalid username or password")
                return render(request, "user/login.html", context={"form":form})
            
@login_required(login_url="login-view")
def logout_view(request):
    logout(request)
    return redirect("main-page")
