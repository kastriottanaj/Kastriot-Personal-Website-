from django.db import models

# Create your models here.
class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(upload_to='industry_icons/', null=True, blank=True)
    description = models.TextField(help_text="Intro paragraph for this business function")

    def __str__(self):
        return self.name
    

class UseCase(models.Model):
    industry = models.ForeignKey(Industry, related_name='use_cases', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.industry.name} - {self.title}"
    
