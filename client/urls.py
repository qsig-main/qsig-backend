from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'), # flipped
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('pitch/', views.PitchList.as_view(), name = 'client-pitch-list'),
    path('pitch/<int:pk>/', views.PitchDetail.as_view(), name = 'client-pitch-detail'),
    path('pitch/create/', views.PitchCreate.as_view(), name='client-pitch-create'),
    path('pitch/<int:pk>/delete/', views.PitchDelete.as_view(), name='client-pitch-delete'),
    path('pitch/img/', views.PitchImageList.as_view(), name = 'client-pitch-image-list'),
    path('pitch/img/<int:pk>/', views.PitchImageDetail.as_view(), name = 'client-pitch-image-detail'),
    path('pitch/img/create/', views.PitchImageCreate.as_view(), name='client-pitch-image-create'),
    path('pitch/img/<int:pk>/delete/', views.PitchImageDelete.as_view(), name='client-pitch-image-delete'),
    path('report/', views.ReportList.as_view(), name = 'client-report-list'),
    path('report/<int:pk>/', views.ReportDetail.as_view(), name = 'client-report-detail'),
    path('report/create/', views.ReportCreate.as_view(), name='client-report-create'),
    path('report/<int:pk>/delete/', views.ReportDelete.as_view(), name='client-report-delete'),
    path('report/img/', views.ReportImageList.as_view(), name = 'client-report-image-list'),
    path('report/img/<int:pk>/', views.ReportImageDetail.as_view(), name = 'client-report-image-detail'),
    path('report/img/create/', views.ReportImageCreate.as_view(), name='client-report-image-create'),
    path('report/img/<int:pk>/delete/', views.ReportImageDelete.as_view(), name='client-report-image-delete'),
    path('member/', views.MemberList.as_view(), name='client-member-list'),
    path('member/position/', views.MemberListPosition.as_view(), name='client-member-list-position'),
    path('member/<int:pk>/', views.MemberDetail.as_view(), name='client-member-detail'),
    path('member/create/', views.MemberCreate.as_view(), name='client-member-create'),
    path('member/<int:pk>/delete/', views.MemberDelete.as_view(), name='client-member-delete'),
    path('wrong/', views.wrong_file_type, name='wrong-file-type'),
]
