from django.urls import path
from tasks_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/add_new', views.add_new, name='add_task'),
    path('tasks/edit/<int:task_id>', views.edit_task, name='edit_task'),
]
