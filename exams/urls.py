from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/', views.exam_list, name='exam_list_alt'), # keep for backward compatibility or direct link
    path('exam/add/', views.exam_create, name='exam_create'),
    path('exam/<int:key>/edit/', views.exam_edit, name='exam_edit'),
    
    path('groups/', views.group_list, name='group_list'),
    path('groups/add/', views.group_create, name='group_create'),
    path('groups/<int:pk>/edit/', views.group_edit, name='group_edit'),
]
