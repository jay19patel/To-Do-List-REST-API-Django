from django.urls import path
from . import views


urlpatterns = [
    path('', views.myapi, name="myapi"),  
    path('taskget/<str:id>/', views.taskget, name="taskget"),  
    path('taskadd/', views.taskadd, name="taskadd"),  
    path('taskupdate/<str:id>/', views.taskupdate, name="taskupdate"),  
    path('taskdelete/<str:id>/', views.taskdelete, name="taskdelete"),  


   
]