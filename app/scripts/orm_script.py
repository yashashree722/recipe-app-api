from app.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint


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
    # print(Rating.objects.filter(rating__gte=9).count())
    # res =Rating.objects.exclude(rating__gte=9)
    # pprint(res.count())
    
    # res = Restaurant.objects.all()
    # pprint(res)
    # pprint(connection.queries)
    
    
    #  query related field 
    # res = Rating.objects.first()
    # print(res.restaurant.name)
    
    # pprint(connection.queries)
    
    # rate = Rating.objects.first()   
    # print(rate.restaurant.name)
    
    # res = Restaurant.objects.first()
    # print(res.ratings.all()) 
    
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.last(),
    #     income = 44.0,
    #     datetime = timezone.now()
    # )
    # # print(connection.queries)
    # res = Restaurant.objects.first()
    # print(res.sales.all())
    
    # user = User.objects.first()
    # restaurant = Restaurant.objects.first()
    # rating , created = Rating.objects.get_or_create(
    #     restaurant = restaurant,
    #     user = user,
    #     rating =1
    # )
    # if created:
    #     print('created')
    # else:
    #     print('not created')
    # pprint(connection.queries)
    #  rating = Rating(
    #     restaurant = Restaurant.objects.first(),
    #     user = User.objects.first(),
    #     rating = 11
    # )
    #  rating.full_clean() # this will run the validators
    #  rating.save()
    
    # res = Restaurant.objects.first()
    # print(res.name)
    # res.name ='yashaashree cafe'
    # res.save(update_fields=['name'])
    # pprint(connection.queries)
    
    
    
    # checking if  models is added or updated _state.adding
    
    # res = Restaurant.objects.all()
    # res .update(
    #     date_opened = timezone.now(),
    # )
    # # res.save()
    
    
    # res = Restaurant.objects.filter(name__startswith='y')
    # print(res)
    # res .update(
    #     date_opened = timezone.now() - timezone.timedelta(days=365),
    # )
    # # res.save()
    # print(connection.queries)
    
    
    # res = Restaurant.objects.first()
    # print(res.pk)
    # print(res.ratings.all())
    # print(res.delete())
    # print(connection.queries)
    
    # print(Restaurant.objects.filter(restaurant_type = Restaurant.TypeChoices.CHINESE) ) 
    
    
    # print(Restaurant.objects.filter(name ='Pizzeria 2') ) 
    # print(Restaurant.objects.get(name ='Pizzeria 2') ) 
    
    
    #  example of AND 
    # res = Restaurant.objects.filter(
    #     restaurant_type = Restaurant.TypeChoices.CHINESE,
    #     name__startswith = 'C',
    # )
    
    # print(res)
    
    
    #  IN filter 
    ch = Restaurant.TypeChoices.CHINESE
    mx = Restaurant.TypeChoices.MEXICAN
    it = Restaurant.TypeChoices.ITALIAN 
    check_types = [ch, mx, it]
    res = Restaurant.objects.filter(
    restaurant_type__in = check_types,
    )
    print(res)
    
    
    
    
    







    
    
    
    
    
    
    # restaurant.save()