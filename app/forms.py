from django import forms
from .models import Restaurant, Rating, Sale  
  

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','restaurant_type')
        
        
        #  maze cha ges 
       