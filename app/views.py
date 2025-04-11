from django.shortcuts import render
from .models import Restaurant,Sale
from django.db.models import Prefetch
from django.utils import timezone

# Create your views here.

def index(request):
    # res = Restaurant.objects.only('rating' , 'restaurant__name').prefetch_related('ratings')   
    # context = {'restaurants': res}
    # return render(request, 'index.html', context)
    #  get all the 5 start rating  and fetch all the restaurant sales with 5 start rating
    
    # res =Restaurant.objects.prefetch_related('ratings' ,'sales' ).filter(ratings__rating=5)
    # print(res)
    
    
    # PREFETCH  OBJECT 
    month_ago = timezone.now() - timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        qs =Sale.objects.filter(date__gte=month_ago),
        
    )
    res =Restaurant.objects.prefetch_related('ratings' ,monthly_sales ).filter(ratings__rating=5)
    # print(res)
    