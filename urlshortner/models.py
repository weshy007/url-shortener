from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"