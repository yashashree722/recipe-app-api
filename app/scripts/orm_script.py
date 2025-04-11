from app.models import Restaurant, Rating, Sale,Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import  Upper, Lower,Length
from django.db.models import Count,Avg, Sum, Min, Max
from django.utils import timezone
from datetime import timedelta


def run():
    # one_moth_ago = timezone.now() - timedelta(days=30)
    # sale  = Sale.objects.filter(datetime__gte=one_moth_ago)
    # print(sale.aggregate(total_income = Sum('income')))
    
    # print(Restaurant.objects.aggregate(total =Count('id')))
    # print(Rating.objects.aggregate(avgs_val =Avg('rating')))
    
    # ans =   Sale.objects.filter(
    #     restaurant__restaurant_type = Restaurant.TypeChoices.CHINESE
    # ).aggregate(min= Min('income'))
    # print(ans)
    # # indexing of rows 
    # # restaurant = Restaurant.objects.all()[0]
    # # print(restaurant)
    # # print(connection.queries)
    
    # #  create object with models.objects.create () method 
    # # Restaurant.objects.create(
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
    # ch = Restaurant.TypeChoices.CHINESE
    # mx = Restaurant.TypeChoices.MEXICAN
    # it = Restaurant.TypeChoices.ITALIAN 
    # check_types = [ch, mx, it]
    # res = Restaurant.objects.filter(
    # restaurant_type__in = check_types,
    # )
    # print(res)
    
    
    #  exclude example 
    # ch = Restaurant.TypeChoices.CHINESE
    # In = Restaurant.TypeChoices.INDIAN
    # mx = Restaurant.TypeChoices.MEXICAN
    # res = Restaurant.objects.exclude(
    #     restaurant_type__in =[ch, In, mx]
    # )
    # print(res)    
    
    
    #  filtering with gt and lt
    #  get the restaursnt which are name begin with A ,B ,C     
    
#    print( Restaurant.objects.filter(
#         name__lt ='E'
#     ))
    
    #    print( Restaurant.objects.filter(
    #     longitude__gt =0
    # ))
    
    #  range lookup 
    
    
    # sales = Sale.objects.filter(
    #     income__range =(50,60)
    # )
    # print( [s.income for s in sales])
    
    
    
    #  oder  by function
    # res = Restaurant.objects.order_by('name').reverse()
    # print(res)
    
    #  indexing
    # res  = Restaurant.objects.order_by('date_opened')[3:4]
    # print(res)
    
    
        # res  = Restaurant.objects.all()
        # print(res)
        
        
        # # earlieest and latest functions in django 
        # In Django, the earliest() and latest() functions are used to retrieve the oldest and 
        # most recent objects from a database based on 
        # a specified field, respectively.
        
        # res = Restaurant.objects.earliest('date_opened')
        # print(res)
        
        # res1 = Restaurant.objects.latest('date_opened')
        # print(res1)
        
        #  filterinng by Foreign key value 
        # #  eg find all ratings associated with res begin with  'C'
        # my_res =Rating.objects.filter(
        # restaurant__name__startswith ='C'
        # )
        # print(my_res)
        
        # staff , created  = Staff.objects.get_or_create(name ='John Doe')
        # print(staff)
        # # print(type(staff.restaurants))
        # # add, all , count , remove , set , clear , create , filter 
        
        # # 
        # staff.restaurants.add(
        #     Restaurant.objects.first(),
        # Restaurant.objects.last()
        # )
        
        # staff.restaurants.set(Restaurant.objects.all()[:5])
        
       

        # StaffRestaurant.objects.create(
        #     staff = staff,
        #     restaurant = Restaurant.objects.first(),
        #     salary = 3000.0
        # )
        # StaffRestaurant.objects.create(
        #     staff = staff,
        #     restaurant = Restaurant.objects.last(),
        #     salary = 3000.0
        # )
        
        
        #  value () method will always return a list of dictionaries
        # res = Restaurant.objects.values(name_upper = Upper('name'))[:3]
        # print(res)
        # print(connection.queries)
        
        
        #  getting related filed with using value ()
        # IT = Restaurant.TypeChoices.ITALIAN
        # raatings = Rating.objects.filter(restaurant__restaurant_type = IT).values(
        #     'restaurant__name',
        #     'rating'
        # )
        # print(raatings)
        
        
        #  value_list () : instead of returning a dictionary it return tuple
        # # flat = True will return a  list
        # res = Restaurant.objects.values_list('latitude',flat=True)
        # print(res)
        
        # Annotating  models = when we want result for each item in qs use annotate 
        # eg : we want all res and wanted to get total number of char in each Restaurant
        # use annotate in this case as we are running query for each restaurant
        # res = Restaurant.objects.annotate(
        #     name_length = Length('name')
        # ).filter(
        #     name_length__gt = 5
        # ).order_by('-name_length')
        # print(res.values('name_length'))
        
        
        # res = Restaurant.objects.annotate(
        #     total_sale = Sum('sales__income') ,
        #     avg_ratings = Avg('ratings__rating')
        # )
        # print(res.values('name','total_sale','avg_ratings'))
        # # print(connection.queries)  
         
         
         
        #  if we use values before annotate theen its going to group by the fields we are using in values
        res = Restaurant.objects.values('restaurant_type').annotate(
            num_rate =  Count('ratings')
        )
        print(res.values('restaurant_type','num_rate'))
        












    
    
    
    
    
    
    # restaurant.save()