# posts/urls.py
from django.urls import path
from app1 import views as app1_views
from .views import profileshow

urlpatterns = [
    path('', app1_views.profileshow, name='profile'),
]