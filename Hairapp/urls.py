from django.urls import path
from . import views
from .views import (SalonList,
    SalonDetail,
    SalonUpdate, 
    SalonDelete, 
    ServiceUpdate,
    )

urlpatterns = [
    path('', views.index, name=('index')),
    path('home', SalonList.as_view(), name = 'Userhome'),
    path('yoursalon', views.yoursalon, name='yoursalon'),
    path('yoursalon/reservations', views.reservations, name='reservations'),
    # path('yoursalon/<str:salon>/reservations', GetReservation.as_view(), name='reservations'),
    path('salon/<int:pk>', SalonDetail.as_view(), name = 'salon-detail'),
    # path('reserve/<int:pk>', SalonReserve.as_view(), name='salon-reserve'),
    # path('salon/new', SalonCreate.as_view(), name = 'salon-create'),
    path('salon/<int:pk>/update', SalonUpdate.as_view(), name = 'salon-update'),
    path('salon/<int:pk>/update/services', ServiceUpdate.as_view(), name = 'service-update'),
    path('salon/<int:pk>/delete', SalonDelete.as_view(), name = 'salon-delete'),

    # path('yoursalon/openess',views.openess , name = 'openess'),

]