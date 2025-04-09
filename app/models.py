from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator
from django.forms import ValidationError

# restaurant model


def validate_bagin_a(value):
    if not value.startswith('a'):
        raise ValidationError(
           'This field must start with "a"',
        )
    
class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN  ='IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK   = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'
            
    name = models.CharField(max_length=100, validators=[validate_bagin_a])
    website = models.URLField(default='')
    date_opened = models.DateField(auto_now_add=True)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90),
        MaxValueValidator(90)],
        null=True, blank=True
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180),
        MaxValueValidator(180)],
        null=True, blank=True   
    )
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
    
    def __str__(self):
        return self.name
    
# user mode
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)]
    )
    
    def __str__(self):
        return f"ratings: {self.rating}"
    
    
    

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null= True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
    
    

    
    