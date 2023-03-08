from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CardUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=400, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    cover_picture = models.ImageField(upload_to='cover_pictures')

    def __str__(self):
        return self.name
    
class SocialLinksIntems(models.Model):
    card_user = models.ForeignKey(CardUser, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=400, null=True, blank=True)
    social_link = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return f"{self.card_user} - {self.social_name}"