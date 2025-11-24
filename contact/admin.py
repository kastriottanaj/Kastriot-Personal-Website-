from django.contrib import admin
from .models import ContactMessage
# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'submitted_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)
