from django.db import models

# Create your models here.
class CardUser(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    cover_picture = models.ImageField(upload_to='cover_pictures')

    def __str__(self):
        return self.name