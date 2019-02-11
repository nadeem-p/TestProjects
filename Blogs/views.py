from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blogs/home.html', context)

def About(request):
    return render(request, 'Blogs/about.html')
