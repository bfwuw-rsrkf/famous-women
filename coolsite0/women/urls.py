from django.urls import path
from women.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<slug:post_slug>', show_post, name='post'),
    path('add_page', add_page, name='add_page'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
]
