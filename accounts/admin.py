from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Department, Role


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'created_at'
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'Organization Information',
            {
                'fields': (
                    'department',
                    'role',
                    'phone',
                    'status'
                )
            }
        ),
    )