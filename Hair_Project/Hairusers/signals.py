from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserPage

@receiver(post_save, sender = User)
def create_page(sender, instance, created, **kwargs):
    if created:
        UserPage.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_page(sender, instance, **kwargs):
    instance.userpage.save()