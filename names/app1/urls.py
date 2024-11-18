from django.urls import path

from . import views

urlpatterns = [
    path("kassim/",views.greeting,name=""),
    path("", views.display)
]
