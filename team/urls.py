from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list_view, name='member-list'),
    path('create/', views.member_create_view, name='member-create'),
    path('<int:pk>/', views.member_detail_view, name='member-detail'),
    path('<int:pk>/update/', views.member_update_view, name='member-update'),
    path('<int:pk>/delete/', views.member_destroy_view, name='member-destroy'),
]
