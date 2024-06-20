from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('logout/', views.logout, name='logout'),
    path('', views.main_page, name='main_page'),
]