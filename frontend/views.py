from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def blog(request):
    return render(request, 'frontend/blog.html')

def cases(request):
    return render(request, 'frontend/cases.html')