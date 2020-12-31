from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' #means select all variables in order function in views.py
        #if you want to select anyone say product you can use field = ['product']
