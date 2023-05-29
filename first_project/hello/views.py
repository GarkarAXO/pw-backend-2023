from django.shortcuts import render
# se importa HttpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "hello/index.html")

# def author(request):
#     return HttpResponse("Autor: Erick Axel Garcia 🧑")

def author(request):
    return HttpResponse("Hello Author 👨‍🎤")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitilize()
    })
