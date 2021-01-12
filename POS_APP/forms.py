from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity','receive_quantity','received_by','issue_quantity','date_added']