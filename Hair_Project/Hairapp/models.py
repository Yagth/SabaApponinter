from django.db import models
from django.contrib.auth.models import User
from Hairusers.models import UserPage
from django.urls import reverse
from PIL import Image

class HairSalon(models.Model):
    salon = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='None')
    rating = models.IntegerField(default=3)
    rators = models.IntegerField(default=0)
    total_customers = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default='Ethiopia')
    iligiblity = models.BooleanField(default=False)
    is_open = models.CharField(max_length=1,choices=[('O','Opened'),('C','Closed')], default='C')
    salon_image = models.ImageField(default='defaultS.jpg', upload_to = 'salons_pics')
    crediblity = models.IntegerField(default=2)

    def __str__(self):
        return f"{self.salon.username}'s salon"

    def get_absolute_url(self):
        return reverse('salon-update', kwargs={'pk':self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.salon_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.salon_image.path)

class Services(models.Model):
    host = models.ForeignKey(HairSalon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()

class Reservations(models.Model):
    host = models.ForeignKey(HairSalon, on_delete=models.CASCADE)
    reserver = models.ForeignKey(User, on_delete=models.CASCADE)
    reserve_type = models.CharField(max_length=100, default="None")
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.host.name}'s reservations"

    

