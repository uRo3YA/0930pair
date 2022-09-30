from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()
    context = {"review": review}
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

    return redirect("test0930:index")
