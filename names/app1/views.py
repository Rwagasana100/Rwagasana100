from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def greeting(request):
  return render(request, "youname.html", {'name': 'Rwagasana elisa'})

def display(request):
  return HttpResponse("Hello")
  