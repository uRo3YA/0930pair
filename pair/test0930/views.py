from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()
    posts = Review.objects.order_by("id")

    context = {
        "review": review,
        "posts": posts,
    }

    # return render(request, "test0930/index.html")
    return render(request, "test0930/index.html", context)


def create(request):

    # 1. parameter로 날라온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 2. DB에 저장
    Review.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    return redirect('test0930:index')

def new(request):

    return render(request,'test0930/new.html')

def detail(request,id):

    post = Review.objects.get(id=id)
    context = {"post":post }


    return render(request,'test0930/detail.html',context)

def delete(request,id):

    post = Review.objects.get(id=id)
    post.delete()

    return redirect('test0930:index')

def edit(request,id):

    post = Review.objects.get(id=id)
    context={
        'post':post
    }

    return render(request, 'test0930/edit.html', context)

def update(request,id):

    post = Review.objects.get(id=id)

    title_ = request.GET.get("title")
    content_ = request.GET.get("content")
    post.title = title_
    post.content = content_
    post.save()


    return redirect('test0930:detail', post.id)