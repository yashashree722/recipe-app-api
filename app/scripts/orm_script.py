from app.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection


def run():
    # indexing of rows 
    # restaurant = Restaurant.objects.all()[0]
    # print(restaurant)
    # print(connection.queries)
    
    #  create object with models.objects.create () method 
    # Restaurant.objects.create(
    #     name = 'Restaurant 1',
    #     date_opened = timezone.now(),
    #     restaurant_type = Restaurant.TypeChoices.OTHER,
    #     latitude = 12.3,
    #     longitude = 98.2,
        
        
    # )
    # print(connection.queries)
    # print(Restaurant.objects.all())
    # print(Restaurant.objects.count())
    # print(Restaurant.objects.last())
    
    
    # #  create a data for ratings Table 
    # restaurant = Restaurant.objects.first()
    # user = User.objects.first()
    # print(user)
    
    # Rating.objects.create(
    #     user = user,
    #     restaurant = restaurant,
    #     rating = 5
    # )
    print(Rating.objects.filter(rating=5))
    
    
    

    
    
    
    
    
    
    # restaurant.save()