from django.urls import path
from women.views import index, about, categories, name_woman

urlpatterns = [
    path('index/', index),
    path('about/', about),
    path('cats/<int:cats_id>/', categories),
    path('name/<str:name>/', name_woman)
]
