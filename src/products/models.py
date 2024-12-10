from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    """
    Represents a product in the system.
    Stores basic product information including product name, image, price and timestamps.
    """
    name = models.CharField(max_length=120, blank=False, help_text='Product\'s name')
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='in US dollars $',
        validators=[MinValueValidator(0)]
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.created_at.strftime('%d/%m/%Y')}"

