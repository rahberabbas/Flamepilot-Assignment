from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.core.validators import RegexValidator


User = get_user_model()


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone_number = models.CharField(max_length=12, validators=[phone_regex], null=True, blank=True)


    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
	    instance.profile.save()