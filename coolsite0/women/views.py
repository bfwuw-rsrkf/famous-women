from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')


def about(request):
    return HttpResponse("<h1>Hello!<h1>My name is Choro.<h1>I'm 17 years old.")
