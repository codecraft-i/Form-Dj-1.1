from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('successfully/', success_view, name='successfully'),
]