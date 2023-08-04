from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from women.models import Woman, Category
from women.forms import AddPostForm


# CRUD request - create, retrieve, update, delete
# Create - post запрос
# Retrieve - get запрос
# Update - put запрос
# Delete - delete запрос


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]


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
    posts = Woman.objects.filter(cat_id=cat_id, is_published=True)
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


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPostForm()
    context = {'form': form, 'menu': menu, 'title': 'Добавление статьи'}
    return render(request, 'add_page.html', context=context)


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Войти')
