from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Department, Role
from .models import Permission

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code"
    )

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

    filter_horizontal = (
        'permissions',
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