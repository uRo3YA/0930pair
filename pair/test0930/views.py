from django.shortcuts import render
#from .models import Review
# Create your views here.
def index(request):
    #review = Review.objects.all()
    #context = {"review": review}
    return render(request, "test0930/index.html")
    #return render(request, "test0930/index.html", context)