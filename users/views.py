from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        return HttpResponse("corno")


"""def register(request):
    return HttpResponse("Estou aqui no cadastro")"""
