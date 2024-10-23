from django.contrib import admin
from django.urls import path, re_path
from .views import TaskCreate


urlpatterns = [
    path('task/', TaskCreate.as_view(), name='task_create'),
    path('task/put/<int:pk>/', TaskCreate.as_view(), name='task_put'),
    # path('task/patch/<int:pk>/', TaskCreate.as_view(), name='task_patch'),
    path('task/delete/<int:pk>/', TaskCreate.as_view(), name='task_patch'),
]
