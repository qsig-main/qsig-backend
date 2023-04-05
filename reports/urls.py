from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list_view, name='report-list'),
    path('create/', views.report_create_view, name='report-create'),
    path('<int:pk>/', views.report_detail_view, name='report-detail'),
    path('<int:pk>/update/', views.report_update_view, name='report-update'),
    path('<int:pk>/delete/', views.report_destroy_view, name='report-destroy'),

    path('img/', views.report_image_list_view, name='report-image-list'),
    path('img/create/', views.report_image_create_view, name='report-image-create'),
    path('img/<int:pk>/', views.report_image_detail_view, name='report-image-detail'),
    path('img/<int:pk>/update/', views.report_image_update_view, name='report-image-update'),
    path('img/<int:pk>/delete/', views.report_image_destroy_view, name='report-image-destroy'),
]
