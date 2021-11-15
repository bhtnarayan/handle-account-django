from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from autoslug import AutoSlugField

# Create your models here.

class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    OTHERS = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user', default = "")
    bio = models.TextField(max_length = 255, blank = True) 
    location = models.CharField(max_length = 55, blank = True) 
    birthdate = models.DateField(null=True, blank = True) 
    gender = models.PositiveSmallIntegerField(choices = GENDER_CHOICES, null = True, blank = True) 
    images = models.ImageField(upload_to = "profile_picture/", default = "profile_picture/default.png", null = True, blank = True) 

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return "/accounts/{}".format(self.slug) 

@receiver(post_save, sender = User) 
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance) 

@receiver(post_save, sender = User) 
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()