from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar_gallery', default='default.jpg')
    telephone = models.CharField(max_length=10)
    


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name='avatar')
#     avatar = models.ImageField(upload_to='avatar_gallery', default='default.jpg')


#     def __str__(self):
#         return f"{self.user.username}'s profile" 


# class Following(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     following = models.ForeignKey(get_user_model(), related_name='following', on_delete=models.DO_NOTHING)

