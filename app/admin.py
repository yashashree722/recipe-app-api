from django.contrib import admin

# Register your models here.
from .models import Restaurant, Rating, Sale,Staff

admin.site.register(Restaurant)
admin.site.register(Rating)
admin.site.register(Sale)
admin.site.register(Staff)



#  admin creenatila 
#  name = 'admin' pass = 123