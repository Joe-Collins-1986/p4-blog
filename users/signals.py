from django.db.models.signals import post_save  # looks for save signal
from django.contrib.auth.models import User  # sender signal
from django.dispatch import receiver  # reciever signal
from .models import Profile  # required as we will be creating a profile in our function


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()