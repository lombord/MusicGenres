from django.urls import path

from .views import *

app_name = 'pop'

urlpatterns = [
    path('', singersPage, name='home'),
    path('singer/<slug:slug>/', singerPage, name='singer'),
]
