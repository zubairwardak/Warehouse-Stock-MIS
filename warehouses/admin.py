from django.contrib import admin
from .models import Warehouse, StorageLocation


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        'code',
        'name',
        'manager',
        'status'
    )



@admin.register(StorageLocation)
class StorageLocationAdmin(admin.ModelAdmin):

    list_display = (
        'warehouse',
        'name'
    )