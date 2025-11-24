from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber

# Register your models here.
admin.site.site_header = "PolePosition Automation"
admin.site.site_title = "PolePosition Automation Admin"
admin.site.index_title = "Welcome to PolePosition Automation Admin Panel"

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

admin.site.register(NewsletterSubscriber)