from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserPage
from Hairapp.models import Reservations
from PIL import Image

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username','email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username','email']

class HostPageUpdateForm(forms.ModelForm):
    class Meta:
        model = UserPage
        fields = ['image','phone_number','hairsalon',]


class CustomerPageUpdateForm(forms.ModelForm):
    class Meta:
        model = UserPage
        fields = ['image','phone_number','status']

        def save(self):
            super().save()
            
            img = Image.open(self.image.path)
            
            if img.height >300 or img.width >300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)