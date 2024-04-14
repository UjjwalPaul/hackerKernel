from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('addUser',views.addUser),
    path('submitUserData', views.submitUserData),
    path('addTask', views.addTask),
    path('submitTaskData', views.submitTaskData),
    path('userManager', views.userManager),
    path('taskManager', views.taskManager),
    path('delete_user/<int:id>', views.delete_user),
    path('delete_task/<int:id>', views.delete_task),
    
    
       
]
