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
        print(mutable_data_copy)
        order_vehicle = mutable_data_copy.get('order')
        print(f'order vehicle = {order_vehicle}')
        number_ordered = int(mutable_data_copy.get('number'))
        vehicle_in_inventory = Vehicle.objects.get(type = order_vehicle.type)
        serializer = self.get_serializer(data=mutable_data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        vehicle_in_inventory.number_in_stock -= number_ordered
        vehicle_in_inventory.save()
        return Response(serializer.data)


        #     def create(self, request):
        # mutable_data_copy = request.data.copy()
        # item_id = mutable_data_copy.get('item')
        # qty_ordered = int(mutable_data_copy.get('qty'))
        # item = Inventory.objects.get(pk=item_id)
        # serializer = self.get_serializer(data=mutable_data_copy)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # item.in_stock -= qty_ordered
        # item.save()
        # return Response(serializer.data)