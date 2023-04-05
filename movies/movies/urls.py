"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Api.views import MovieLst,MovieItem,MovieModellist,MovieMitem,UserCreationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies',MovieLst.as_view()),
    path('movies/<int:mid>',MovieItem.as_view()),
    path('mv/<int:mid>',MovieMitem.as_view()),
    path('user',UserCreationView.as_view()),
    
    path('mv/',MovieModellist.as_view())
    
    
]
