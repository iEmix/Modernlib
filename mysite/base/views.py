from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'base.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')

def test(request):
    return HttpResponse("test")