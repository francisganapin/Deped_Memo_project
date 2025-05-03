from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin-page/', views.memo_views, name='memo_views'),
    path('admin-page/check_memo/page/<int:id>',views.memo_check_view,name='memo_check_view'),
    path('admin-page/page2/upload_memo/', views.memo_upload_views, name='memo_upload_views'),
    path('admin-page//page2/delete_memo/',views.memo_delete_view,name='memo_delete_views'),
    path('admin-page/page2/update_memo/<int:id>',views.memo_update_views,name='memo_update_views')
   
]

# Serve media files in development mode\


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

