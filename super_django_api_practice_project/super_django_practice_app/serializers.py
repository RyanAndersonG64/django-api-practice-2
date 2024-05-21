from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'type', 'number_in_stock']

class CustomerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'bicycles_owned', 'tricycles_owned', 'unicycles_owned', 'mountain_bikes_owned', 'bmx_bikes_owned']

class CustomerOrderSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'customer', 'order', 'created_date', 'number', 'paid']

