from django.shortcuts import render
from women.models import Woman, Category
from django.http import Http404


# CRUD request - create, retrieve, update, delete
# Create - post запрос
# Retrieve - get запрос
# Update - put запрос
# Delete - delete запрос


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Woman.objects.filter(is_published=True)
    cats = Category.objects.all()
    data = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request, 'index.html', data)


def about(request):
    data = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'index.html', data)


def show_category(request, cat_id):
    posts = Woman.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'index.html', context=context)
