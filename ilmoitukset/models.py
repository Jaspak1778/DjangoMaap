#models.py 
#path : E:\Koodi\DJANGO\kauppatoriapp\ilmoitukset\models.py

from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Tämä kenttä on valinnainen
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)  # Kuvan kenttä

    def __str__(self):
        return self.title


