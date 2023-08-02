from django.shortcuts import render, get_object_or_404
from women.models import *


# CRUD request - create, retrieve, update, delete
# Create - post запрос
# Retrieve - get запрос
# Update - put запрос
# Delete - delete запрос


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Woman.objects.filter(is_published=True)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'index.html', data)


def about(request):
    data = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'index.html', data)


def show_category(request, cat_id):
    posts = Woman.objects.filter(cat_id=cat_id)
    context = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Woman, slug=post_slug)
    context = {
        "title": 'Главная страница',
        "menu": menu,
        "post": post,
        "cat_selected": post.cat_id,
    }
    return render(request, "post.html", context=context)
