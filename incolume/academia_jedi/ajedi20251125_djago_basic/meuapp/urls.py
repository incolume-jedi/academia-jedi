"""URL configuration for meuprojeto project.

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

from django.urls import path

from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('/saudacao/', views.saudacao, name='saudacao'),
    path('/saudacao/<str:nome>/', views.saudacao, name='saudacao'),
    path('/produto/<int:id_produto>', views.produto, name='produto'),
    path('/produtos', views.produtos, name='produtos'),
    path('/index/', views.index, name='index'),
]
