from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

