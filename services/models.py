from django.db import models
from industries.models import Industry
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    industries = models.ManyToManyField(Industry, blank=True, related_name='services')

    def __str__(self):
        return self.title

