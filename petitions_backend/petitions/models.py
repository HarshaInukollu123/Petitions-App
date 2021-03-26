from django.db import models

# Create your models here.

class Petition(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
