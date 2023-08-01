from django.urls import path
from women.views import index, about, show_category

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about),
    path('category/<int:cat_id>/', show_category, name='category'),
]
