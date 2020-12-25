from django.db import models

# Create your models here.
#These will create a model table
#First we have to shut the server down then migrate using command python manage.py makemigrations
#This will create the set of sql commands in the migration folders in accounts app
#Then we will type python manage.py migrate to activate the database we in the above comment
#Now we will register this model database in admin.py file



class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):#This will display the name of the customer when we create in the admin panel instead of customer ID
        return self.name




class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)