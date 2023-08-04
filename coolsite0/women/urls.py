from django.urls import path
from .views import *

urlpatterns = [
    path('index/', HomePageListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<slug:post_slug>', ShowPostDetailView.as_view(), name='post'),
    path('add_page', AddPageCreateView.as_view(), name='add_page'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
]
