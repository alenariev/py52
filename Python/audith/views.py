from django.shortcuts import render

from django.http import HttpResponse

# def index(request):
#     return HttpResponse ("Hello, World")

def index(request):
    print(request.__dict__)
    return render(request, 'audith/index.html')

def about(request):
    print(request.__dict__)
    return render(request, 'about/indexAbout.html')