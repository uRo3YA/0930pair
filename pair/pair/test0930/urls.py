from django.urls import path
from . import views

app_name = "test0930"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("update/<int:id>", views.update, name="update"),



]
