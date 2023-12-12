from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("addreq/", views.addreq, name="addreq"),
    path("update/<int:id>/", views.update, name="update"),
    path("update/upreq/<int:id>/", views.upreq, name="upreq"),
    path("delete/<int:id>/", views.delete, name="delete")
]
