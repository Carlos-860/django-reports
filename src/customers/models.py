from django.db import models

# Create your models here.

class Customer(models.Model):
    """
    Represents a customer in the system.
    Stores basic customer information including business name and logo.
    """
    name = models.CharField(max_length=120, blank=False, help_text='Customer\'s business name')
    logo = models.ImageField(upload_to='customers', default='no_picture.png')

    def __str__(self):
        return self.name