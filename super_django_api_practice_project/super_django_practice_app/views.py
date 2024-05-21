from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from .models import *
from .serializers import *

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSeralizer


class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSeralizer

    def create(self, request):
        mutable_data_copy = request.data.copy()
        order_vehicle = mutable_data_copy.get('order')
        order_vehicle = Vehicle.objects.get(pk=order_vehicle)
        number_ordered = int(mutable_data_copy.get('number'))
        vehicle_in_inventory = Vehicle.objects.get(type = order_vehicle.type)

        if number_ordered > vehicle_in_inventory.number_in_stock:
            raise ValidationError({'There are not enough vehicles in stock for this order'})
        
        serializer = self.get_serializer(data=mutable_data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        vehicle_in_inventory.number_in_stock -= number_ordered
        vehicle_in_inventory.save()
        return Response(serializer.data)
    
    
    def destroy(self, request, pk=None):
        order = self.get_object()
        print(f'order =  {order}')
        if order.paid == True:
            order.customer.vehicles_owned += order.number
        else:
            order.order.number_in_stock += order.number
        self.perform_destroy(order)
        print('DELORTED')
        return Response