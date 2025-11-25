from django.contrib import admin
from .models import BlogPost, Category
from taggit.models import Tag

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "published")
    search_fields = ("title",)
    list_filter = ("published", "created_at")
    ordering = ("-created_at",)
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "meta_title", "meta_description", "content", "category", "featured_image", "author", "published", "tags")



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
