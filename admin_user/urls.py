from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('page2/', views.memo_views, name='memo_views'),
    path('page2/upload_memo/', views.memo_upload_views, name='memo_upload_views'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

