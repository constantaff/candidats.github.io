"""kurs_chern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
    path('', views.index, name='index'),
    path('votes/', views.votes, name='votes'),
    path('login/', views.login_page, name='login'),
    path('try-login/', views.try_login, name='try-login'),
    path('try-register/', views.try_register, name='try-register'),
    path('add-vote/<int:elect_id>/', views.add_vote, name='add-vote'),
    path('donate/', views.donate, name='donate'),
]
