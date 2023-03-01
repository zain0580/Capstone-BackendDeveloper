from django.shortcuts import render,HttpResponse
from .serializers import MenuItemsSerializer,BookingSerializer
from .models import Menu,Booking

# DRF views
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
# DRF authentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
#----------------------------------------------------------------------------------


# for Function based
# @api_view()
# @permission_classes([IsAuthenticated])
def index(request):
    return render(request,"index.html")


# for class based views
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemsSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemsSerializer

class BookingsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer