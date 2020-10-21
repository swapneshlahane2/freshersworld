"""freshersworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from jobsapp import views
from django.contrib.auth import views as auth_view   # for login and logout operation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootstrap/', views.bootstrap_view),
    path('software/', views.software_view),
    path('pharma/',views.pharma_view),
    path('agriculture/', views.agriculture_view),
    path('add/', views.add_view),
    path('update/<int:id>/', views.update_view),
    path('delete/<int:id>/', views.delete),
    path('showsoftwarejobs/',views.show_software_view),
    path('showpharmajobs/', views.show_pharma_view),
    path('showagriculturejobs/',views.show_agriculture_view),
    path('login/', auth_view.LoginView.as_view(template_name='login.html')),
    path('logout/',auth_view.LogoutView.as_view()),
]
