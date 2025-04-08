from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('page1/',views.memo_page1_view,name='memo_page1_views'),
    path('page1/content/<int:id>',views.memo_views_content,name='memo_views_content'),
    path('page2/', views.memo_views, name='memo_views'),
    path('page2/upload_memo/', views.memo_upload_views, name='memo_upload_views'),
    path('page2/delete_memo/',views.memo_delete_view,name='memo_delete_views')
   
]

# Serve media files in development mode\


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

