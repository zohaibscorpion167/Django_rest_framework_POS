from django.contrib import admin
from django.contrib.auth.models import Group



# Register your models here.
from .models import Stock, Restaurant
from .forms import StockCreateForm
from import_export.admin import ImportExportModelAdmin




# class StockCreateAdmin(admin.ModelAdmin):

# admin.site.register(Restaurant)


admin.site.unregister(Group)


@admin.register(Restaurant)
class ExportRes(ImportExportModelAdmin,admin.ModelAdmin):
   list_display = ['Customer_Name','Customer_Number','order_time','order_date','Total_Cost','Status']
   search_fields = ['Customer_Name','order_date','Customer_Number']
   list_filter = ['order_date']
   pass


@admin.register(Stock)
class ExportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity', 'date_added']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']
   pass