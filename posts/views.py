from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
# Create your views here.
def hello_view(request):
    return HttpResponse("hello world")

def html_view(request):
    return render(request,"tea.html")

def main_view(request):
    return render(request, "main.html")

def list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts" : posts})

def detail_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, "posts/post_detail.html", context={"post" : post})
