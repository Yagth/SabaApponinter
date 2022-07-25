from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import HairSalon

@receiver(post_save, sender=User)
def create_salon(sender, instance, created, **kwargs):
    if created:
        HairSalon.objects.create(salon=instance)

@receiver(post_save, sender=User)
def save_salon(sender, instance, **kwargs):
    instance.hairsalon.save()
