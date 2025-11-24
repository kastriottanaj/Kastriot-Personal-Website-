from django.db import models

# Create your models here.
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        help_text="Rating from 1 to 5"
    )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.rating} Stars"