from django.urls import path

from .views import *

app_name = 'rock'

urlpatterns = [
    path('', singersPage, name='home'),
    path('singer/<slug:slug>/', singerPage, name='singer'),
]
