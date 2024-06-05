from django.db import models

# Create your models here.
class postAdd(models.Model):
    name = models.TextField(max_length=20)
    seriya = models.TextField(max_length=20)
    image = models.ImageField(upload_to='image/')