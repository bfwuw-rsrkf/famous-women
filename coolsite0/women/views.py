from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def categories(request, cats_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1> {cats_id}")


def name_woman(request, name):
    return HttpResponse(f"<h1>Женщину зовут {name}.</h1>")
