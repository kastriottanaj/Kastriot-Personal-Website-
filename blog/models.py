from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
     
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=160, help_text="Meta description for SEO")
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_width = models.PositiveIntegerField(null=True, blank=True)
    image_height = models.PositiveIntegerField(null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_title = models.CharField(max_length=70, help_text="Meta title for SEO", blank=True)
    meta_description = models.TextField(max_length=160, help_text="Meta description for SEO", blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager(blank=True)

    def blog_list(request, tag_slug=None):
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            posts = posts.filter(tags__in=[tag])

    def save(self, *args, **kwargs):
        # Slug generation
        if not self.slug:
            self.slug = slugify(self.title)

        # Save initially to ensure the image file is available
        super().save(*args, **kwargs)

        # Image size detection
        if self.featured_image:
            try:
                img = Image.open(self.featured_image.path)
                self.image_width = img.width
                self.image_height = img.height
                super().save(update_fields=["image_width", "image_height"])
            except Exception as e:
                print(f"[Warning] Could not determine image size: {e}")

    def web_image_url(self):
        if self.featured_image:
            return self.featured_image.url.replace(".jpg", ".webp").replace(".png", ".webp")
        return ""
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

    def __str__(self):
        return self.title

class NewsletterSignup(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

