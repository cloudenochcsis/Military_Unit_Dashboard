from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('health/', views.health_check, name='health_check'),
    
    # Soldier URLs
    path('soldiers/', views.soldier_list, name='soldier_list'),
    path('soldiers/<int:pk>/', views.soldier_detail, name='soldier_detail'),
    path('soldiers/add/', views.soldier_create, name='soldier_create'),
    path('soldiers/<int:pk>/edit/', views.soldier_update, name='soldier_update'),
    path('soldiers/<int:pk>/delete/', views.soldier_delete, name='soldier_delete'),
    
    # Equipment URLs
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/add/', views.equipment_create, name='equipment_create'),
    path('equipment/<int:pk>/edit/', views.equipment_update, name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),
]
