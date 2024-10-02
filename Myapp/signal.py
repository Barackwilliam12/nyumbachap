from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Profile, Property

# from . models import Notification 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

