from django.shortcuts import render, HttpResponse

# Create your views here.

def index_page(reguest):
    return HttpResponse('<h1>Hello world</h1>')


def kvadrat(reguest):
    data = {
        'name': 'Coders Azerbaijan',
        'course': 'Python'
    }
    return render(reguest, "index.html",data)