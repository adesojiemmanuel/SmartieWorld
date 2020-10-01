from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import Post, Event
# Create your views here.

def index(request):
    post = Post.objects.all()
    return render(request, 'frontend/index.html', {'pst':post}) 

def about(request):
    return render(request, 'frontend/about.html')

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def event(request):
    event = Event.objects.all()
    return render(request, 'frontend/event.html', {'evt':event})

def cases(request):
    return render(request, 'frontend/cases.html')

