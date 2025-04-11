from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator
from django.forms import ValidationError
from django.db.models.functions import Lower

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
    
    # define defaultt oderring
    class Meta:
        ordering = [Lower('name'),'date_opened']
    
    def __str__(self):
        return self.name
    
    def save(self , *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)
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
    
    def __str__(self):
        return f"Sale: {self.restaurant.name} - {self.income}"
    
    
    
# Restaurant can have many staff members and staff can work in many restaurants 
class Staff(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ManyToManyField(Restaurant, through='StaffRestaurant')
    
    
class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)
    
    
    
    

    
    