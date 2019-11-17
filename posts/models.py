from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='posts_gallery')
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name='images')
    comment = models.CharField(max_length=250)

