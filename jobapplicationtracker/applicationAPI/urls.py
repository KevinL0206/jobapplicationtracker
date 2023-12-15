from . import views
from django.urls import path

urlpatterns = [
    
    path('applications/', views.displayApplications,name = 'display'),
    path('createApplication/', views.createJobApplication, name= 'create'),
    path('editApplication',views.editApplication, name= 'edit')
    
]