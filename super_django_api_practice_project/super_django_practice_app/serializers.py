from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'type', 'number_in_stock']

class CustomerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'vehicles_owned']

class CustomerOrderSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'customer', 'order', 'created_date', 'number', 'paid']

