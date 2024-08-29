from django.db import models


# Create your models here.

class About (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title