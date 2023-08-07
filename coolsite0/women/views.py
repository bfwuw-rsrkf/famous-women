from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Woman
from .forms import AddPostForm
from .utils import DataMixin


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


class HomePageListView(LoginRequiredMixin, DataMixin, ListView):
    model = Woman
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Woman.objects.filter(is_published=True)


def about(request):
    data = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'index.html', data)


class ShowCategoryListView(DataMixin, ListView):
    model = Woman
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Woman.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=f'Категория - {str(context["posts"][0].cat)}',
            cat_selected=context['posts'][0].cat_id
        )
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostDetailView(DataMixin, DetailView):
    model = Woman
    template_name = 'post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPageCreateView(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Войти')
