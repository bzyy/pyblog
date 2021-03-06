"""pyblog URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('post/<uuid:slug>/', views.ArticleDetail.as_view(), name='detail'),
    path('post/<uuid:slug>/comments/', views.Comment.as_view(), name='comment'),
    path('archive', views.Archive.as_view(), name='archive'),
    path('tag/<str:name>/', views.Tag.as_view(), name='tag'),
    path('about', views.AboutMe.as_view(), name='about'),
    path('coffee', views.Coffee.as_view(), name='coffee'),
]

handler404 = views.handler404

