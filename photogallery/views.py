from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def camera(request):
    return render(request,'all-photos/camera.html')
   
def screenshot(request):
    return render(request,'all-photos/screenshot.html')

def download(request):
    return render(request,'all-photos/download.html')

  