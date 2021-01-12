from django.db import models
from datetime import date, datetime
from django.db.models import Avg, Max, Min, Sum


# Create your models here.
class Stock(models.Model):
    category = models.CharField(max_length=50, blank=True, null=False)
    item_name = models.CharField(max_length=50, blank=True, null=False)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateField(default=date.today())
	

    def __str__(self):
        return self.item_name





# Create your models here.
class Restaurant(models.Model):
    Order_ID = models.AutoField( primary_key = True,  verbose_name ='Order ID')
    Customer_Name = models.CharField(max_length=50, blank=False, null=False)
    Customer_Number = models.CharField(max_length=10, blank=True, null=True)
    item_1 = models.CharField(max_length=10,blank=False, null=False)
    item_2 = models.CharField(max_length=10,blank=True, null=True)
    item_3 = models.CharField(max_length=10,blank=True, null=True)
    item_4 = models.CharField(max_length=10,blank=True, null=True)
    item_5 = models.CharField(max_length=10,blank=True, null=True)
    Total_Cost = models.CharField(max_length=5,blank=False, null=False)
    Received_By = models.CharField(max_length=10,blank=False, null=False)
    order_date = models.DateField(default=date.today())
    order_time = models.TimeField(default=datetime.now())
    Status = models.BooleanField("Delivered" ,default=False)


    
    
    def __str__(self):
        return self.Customer_Name