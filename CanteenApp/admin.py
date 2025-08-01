from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel, Company, Branch

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'user_role', 'company', 'branch', 'is_active']
    list_filter = ['user_role', 'is_active', 'company']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Context', {'fields': ('user_role', 'company', 'branch', 'phone')}),
    )

admin.site.register(UserModel, CustomUserAdmin)