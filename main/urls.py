from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('track/', track_page, name='track_page'),
]
