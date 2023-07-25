from django.shortcuts import render
from random import choice
# from django.http import HttpResponse

# CRUD request - create, retrieve, update, delete
# Create - post запрос
# Retrieve - get запрос
# Update - put запрос
# Delete - delete запрос


# def index(request):
#     data = {"header": "Hello, Django!", "message": "Welcome to Python."}
#     return render(request, "index.html", context=data)


def index(request):
    header = "Данные пользователя"  # обычная переменная
    langs = ["Python", "Java", "C#"]  # список
    user = {"name": "Tom", "age": 23}  # словарь
    address = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)


# def about(request):
#     return render(request, "about.html")


def about(request):
    header = "About me"
    user = ["Shulamita", "Sakura", "Naruto", "Hurem", "Hinata", "Erzhan", "Aicholpon", "Killua"]
    langs = ["English", "Russian", "Spanish", "French", "Chinese"]
    address = ("Ottawa", "Ankara", "Madrid", "Konoha", "Rome", "Paris", "Amsterdam")

    data = {"header": header, "user": choice(user), "langs": langs, "address": choice(address)}
    return render(request, "about.html", context=data)


# def categories(request, cats_id):
#     return HttpResponse(f"<h1>Статьи по категориям</h1> {cats_id}")


# def name_woman(request, name):
#     return HttpResponse(f"<h1>Женщину зовут {name}.</h1>")
