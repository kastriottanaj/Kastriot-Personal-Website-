from django.contrib import admin

# Register your models here.
from .models import Industry, UseCase

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(UseCase)
class UseCaseAdmin(admin.ModelAdmin):
    list_display = ("title", "industry")
    search_fields = ("title", "industry__name")
    list_filter = ("industry",)

