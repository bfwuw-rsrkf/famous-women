from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import *
from .models import Woman, Category
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
]


class HomePageListView(DataMixin, ListView):
    model = Woman
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Woman.objects.filter(is_published=True).select_related("cat")


def about(request):
    data = {'menu': menu if request.user.is_authenticated else menu[::2], 'title': 'О сайте'}
    return render(request, 'index.html', data)


class ShowCategoryListView(DataMixin, ListView):
    model = Woman
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Woman.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(
            title=f'Категория - {str(cats.name)}',
            cat_selected=cats.pk
        )
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostDetailView(DataMixin, DetailView):
    model = Woman
    template_name = 'post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['post'],
            cat_selected=context['post'].cat_id
        )
        return dict(list(context.items()) + list(c_def.items()))


class AddPageCreateView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Добавление статьи',
            cat_selected=None
        )
        return dict(list(context.items()) + list(c_def.items()))


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Обратная связь',
            cat_selected=None
        )
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Авторизация',
            cat_selected=None
        )
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Регистрация',
            cat_selected=None
        )
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
