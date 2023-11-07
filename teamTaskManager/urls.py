from django.urls import path

from . import views

urlpatterns = [
    path('task-list', views.task_list, name='task-list'),
    path('task-create', views.task_create, name='task-create'),
    path('task-update/<str:task_id>', views.task_update, name='task-update'),
    path('task-delete/<str:task_id>', views.task_delete, name='task-delete'),
    path('task-toggle-complete/<str:task_id>', views.task_toggle, name='task-toggle'),


    path('worker-list', views.worker_list, name='worker-list'),
    path('worker-create', views.worker_create, name='worker-create'),
    path('worker-update/<str:worker_id>', views.worker_update, name='worker-update'),
    path('worker-delete/<str:worker_id>', views.worker_delete, name='worker-delete'),
    path('worker-toggle-busy/<str:worker_id>', views.worker_toggle, name='worker-toggle'),
]
