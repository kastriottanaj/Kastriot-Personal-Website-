from django.contrib import admin
from .models import Testimonial

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_approved', 'created_at')
    search_fields = ('client_name', 'message')
    list_filter = ('is_approved', 'rating', 'created_at')
    ordering = ('-created_at',)