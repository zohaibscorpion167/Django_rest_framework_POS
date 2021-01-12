from rest_framework import serializers
from .models import Restaurant




class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
    #  fields = ['Customer_Name', 'Customer_Number', 'item_1','item_2','item_3','item_4','item_5','Total_Cost','Received_By','Status']



# class RestaurantSerializer(serializers.Serializer):
#     Customer_Name = serializers.CharField(max_length=50, blank=False, null=False)
#     Customer_Number = serializers.CharField(max_length=10, blank=True, null=True)
#     item_1 = serializers.CharField(max_length=10,blank=False, null=False)
#     item_2 = serializers.CharField(max_length=10,blank=True, null=True)
#     item_3 = serializers.CharField(max_length=10,blank=True, null=True)
#     item_4 = serializers.CharField(max_length=10,blank=True, null=True)
#     item_5 = serializers.CharField(max_length=10,blank=True, null=True)
#     Total_Cost = serializers.CharField(max_length=5,blank=False, null=False)
#     Received_By = serializers.CharField(max_length=10,blank=False, null=False)
#     Status = serializers.BooleanField("Delivered" ,default=False)

    # def create(self,validated_data):
    #     return Restaurant.objects.create(validated_data)


    # def update(self,instance,validated_data):
    #     instance.Customer_Name = validated_data.get('Customer_Name',instance.Customer_Name)
    #     instance.Customer_Number = validated_data.get('Customer_Number',instance.Customer_Number)
    #     instance.item_1 = validated_data.get('item_1',instance.item_1)
    #     instance.item_2 = validated_data.get('item_2',instance.item_2)
    #     instance.item_3 = validated_data.get('item_3',instance.item_3)
    #     instance.item_4 = validated_data.get('item_4',instance.item_4)
    #     instance.item_5 = validated_data.get('item_5',instance.item_5)
    #     instance.Total_Cost = validated_data.get('Total_Cost',instance.Total_Cost)
    #     instance.Received_By = validated_data.get('Received_By',instance.Received_By)
    #     instance.Status = validated_data.get('Status',instance.Status)
    #     instance.save()
    #     return instance




    