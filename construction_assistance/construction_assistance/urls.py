"""
URL configuration for construction_assistance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from facilbuild import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('contra_reg/', views.contra_reg),
     path('worker_reg/' , views.worker_reg),
     path('user_reg/' , views.user_reg),
     path('admin_home/', views.admin_home),
    path('contra_home/', views.contra_home),
    path('worker_home/' , views.worker_home),
    path('user_home/' , views.user_home),
    path('adcont_view/', views.adcont_view),
    path('adwr_view/' , views.adwr_view),
    path('adusr_view/' , views.adusr_view),
]
