from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.forms import Post_Form
from django.contrib.auth.decorators import login_required
# Create your views here.
def hello_view(request):
    return HttpResponse("hello world")

def html_view(request):
    return render(request,"tea.html")

def main_view(request):
    return render(request, "main.html")

@login_required(login_url="login-view")
def list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts" : posts})

@login_required(login_url="login-view")
def detail_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, "posts/post_detail.html", context={"post" : post})

@login_required(login_url="login-view")
def create_post(request):
    if request.method == "GET":
        form = Post_Form()
        return render(request, "posts/post_create.html", context={"form":form})
    if request.method == "POST":
        form = Post_Form(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form":form})
        elif form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            rate = form.cleaned_data["rate"]
            image = form.cleaned_data["image"]
            post = Post.objects.create(title=title, content=content, rate=rate, image=image)
            return redirect("/list_view/")
            
        # data = request.POST
        # image = request.FILES.get("image")
        # title = data.get("title")
        # content = data.get("content")
        # rate = data.get("rate")