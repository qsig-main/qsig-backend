from django.urls import path
from . import views

urlpatterns = [
    path('', views.pitch_list_view, name='pitch-list'),
    path('create/', views.pitch_create_view, name='pitch-create'),
    path('<int:pk>/', views.pitch_detail_view, name='pitch-detail'),
    path('<int:pk>/update/', views.pitch_update_view, name='pitch-update'),
    path('<int:pk>/delete/', views.pitch_destroy_view, name='pitch-destroy'),

    path('img/', views.pitch_image_list_view, name='pitch-image-list'),
    path('img/create/', views.pitch_image_create_view, name='pitch-image-create'),
    path('img/<int:pk>/', views.pitch_image_detail_view, name='pitch-image-detail'),
    path('img/<int:pk>/update/', views.pitch_image_update_view, name='pitch-image-update'),
    path('img/<int:pk>/delete/', views.pitch_image_destroy_view, name='pitch-image-destroy'),
]
