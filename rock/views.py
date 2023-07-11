from django.http import HttpRequest
from django.shortcuts import render

from .models import Singer


def singersPage(request: HttpRequest):
    singers = Singer.objects.all()
    context = {'singers': singers, 'category': 'rock'}
    return render(request, 'singers.html', context)


def singerPage(request: HttpRequest, slug: str):
    singer = Singer.objects.get(slug=slug)
    context = {'singer': singer}
    return render(request, 'singer.html', context)
