"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views as app1_views
from home import views as home_views
from django.conf import settings # new
from rest_framework import routers
from django.conf.urls.static import static # new


router = routers.DefaultRouter()
router.register(r'app1', app1_views.DonateViewSet)
router.register(r'users', app1_views.UserViewSet)
router.register(r'org-name', app1_views.CategoryViewSet)




urlpatterns = [
	path('api/v1/', include(router.urls)),
    path('api-auth/v1/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
	path('', app1_views.home, name='home'),
	path('home/',app1_views.home,name='home'),
	path('project3/static/another.jpg',app1_views.home,name='home'),
	path('project3/templates/poster1.jfif',app1_views.home,name='home'),
	path('project3/templates/poster2.jfif',app1_views.home,name='home'),
	path('project3/templates/poster3.jfif',app1_views.home,name='home'),
	path('join/',app1_views.join,name='join'),
	path('login/',app1_views.user_login,name='user_login'),
	path('logout/', app1_views.user_logout, name='user_logout'),
	path('about/', app1_views.about, name='about'),
	path('who/', app1_views.who, name='who'),
	path('donate/', app1_views.donate, name='donate'),
	path('history/',app1_views.history,name='history'),
	path('user_profile/', app1_views.user_profile,name='Profile'),
	path('dashboard/', app1_views.dashboard, name='dashboard'),
	path('profileshow/',app1_views.profileshow, name='profile'),
	path('project3/media/',app1_views.profileshow,name='about'),
	path('payment/', app1_views.payment, name='pay'),
	path('project3/static/amex.jpg', app1_views.payment, name='payment'),


	#path('', include('app1.urls')), # new  
	   ]


		