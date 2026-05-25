"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shedule/',views.shedule,name='shedule_default'),
    path('shedule/<int:weekId>/',views.shedule,name='shedule'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('name/',views.name, name='name'),
    path('project/',views.project, name='project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contacts/',views.contacts, name='contacts'),
    
    path('fibonacci/', views.fibonacci, name='fibonacci_default'),
    path('fibonacci/<int:amount>/', views.fibonacci, name='fibonacci'),
    path('fibonacci/<int:amount>/<int:numb>/', views.fibonacci, name='fibonacci'),
    
    path('catalog/',views.catalog,name='catalog_default'),
    path('catalog/<int:id>/',views.catalog,name='catalog')
]
