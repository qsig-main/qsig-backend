from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('api.urls')),
    path('api/pitch/', include('pitches.urls')),
    path('api/report/', include('reports.urls')),
    path('client/', include('client.urls')),
    path('api/team/', include('team.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
