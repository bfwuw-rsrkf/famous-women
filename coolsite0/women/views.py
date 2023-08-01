from django.shortcuts import render
from women.models import Woman, Category


# CRUD request - create, retrieve, update, delete
# Create - post запрос
# Retrieve - get запрос
# Update - put запрос
# Delete - delete запрос


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Woman.objects.filter(is_published=True)
    data = {
        'menu': menu,
        'title': 'Главная страница',
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
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'index.html', context=context)
