"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from gestionBook.views import main_hub

from gestionBook.views import BookAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',include('gestionBook.urls')),
    path('',main_hub),
    path('auth0/',include('authentication.urls')),
    path("account/",include('gestionAccount.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/book/', BookAPIView.as_view()),
]
