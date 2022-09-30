from django.urls import path
from . import views

app_name = "test0930"
urlpatterns = [
    path("", views.index, name="index"),

]