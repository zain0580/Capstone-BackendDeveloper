from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.index, name='homepage' ),
    path('menu-items/', views.MenuItemsView.as_view(),name='menuItems'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(),name='singleMenuItem'),
    path('bookings/', views.BookingsView.as_view(),name='bookings'),
    path('bookings/<int:pk>', views.SingleBookingView.as_view(),name='singleBooking'),
    # for token generation
    path('api-token-auth/', obtain_auth_token),
]
