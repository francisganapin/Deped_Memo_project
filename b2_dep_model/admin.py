from django.contrib import admin
from .models import AdminUser

# Register your models here.
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('email','is_staff','is_active','date_joined')
    search_fields = ('email',)

admin.site.register(AdminUser,AdminUserAdmin)