from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='defaultU.jpg', upload_to='User_pics')
    status = models.CharField(max_length=10, choices=[(
        'CUSTOMER', 'CUSTOMER'), ('HOST', 'HOST')], default='CUSTOMER')
    phone_number = models.CharField(max_length=20, default='')
    crediblity = models.IntegerField(default=3)
    hairsalon = models.CharField(max_length=100, default='None')

    def __str__(self):
        return f"{self.user.username}'s Page"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class YourReserv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salon = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f'reservation at {YourReserv.salon}'