from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.memo_page1_view,name='memo_page1_views'),
    path('memo/list-content/page/<int:page_number>/content/<int:id>/id',views.memo_views_content,name='memo_views_content'),
]

# Serve media files in development mode\


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

