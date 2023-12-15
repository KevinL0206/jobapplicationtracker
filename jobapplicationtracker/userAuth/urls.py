from . import views
from django.urls import path

urlpatterns = [
    
    path('register/', views.register,name = 'register'),
    path('login/',views.loginUser, name = 'login'),
    path('home/',views.home, name = 'home'),

]