from django.contrib import admin
from .models import Soldier, Equipment

@admin.register(Soldier)
class SoldierAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'email', 'phone', 'status', 'created_at')
    list_filter = ('status', 'rank')
    search_fields = ('name', 'rank', 'email')
    ordering = ('name',)
    date_hierarchy = 'created_at'

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'serial_number', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'type')
    search_fields = ('name', 'serial_number')
    ordering = ('name',)
    date_hierarchy = 'created_at'
    autocomplete_fields = ['assigned_to']
