"""POS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from POS_APP.views import RestaurantApiView, OrderDetailsApi
 

admin.site.site_header = "Point of Sale"
admin.site.site_title = "Welcome to Point of Sale"
admin.site.index_title = "Welcome to Point of Sale"
admin.site.site_url = None


urlpatterns = [
    path('', admin.site.urls),
    path('orders/', RestaurantApiView.as_view()),
    path('orders/<int:Order_ID>', OrderDetailsApi.as_view()),
]
