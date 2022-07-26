import re
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (ListView,
DetailView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import HairSalon, Reservations, Services


def index(request):
    return render(request, 'index.html')


@login_required
def User_home(request):
    context = {
        'salons': HairSalon.objects.all()
        }

    return render(request, 'user_home.html', context)


class SalonList(LoginRequiredMixin, ListView):
    model = HairSalon
    template_name = 'user_home.html'
    context_object_name = 'salons'
    ordering = ['-rating']
    paginate_by = 2


class SalonDetail(LoginRequiredMixin, DetailView):
    model = HairSalon
    

class SalonUpdate (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HairSalon
    fields = ['location','is_open', 'salon_image']

    def test_func(self):
        salon = self.get_object()
        if self.request.user == salon.salon:
            return True
        return False

    def form_valid(self, form):
            form.instance.salon = self.request.user
            messages.info(self.request, 'Salon Updated successfully')
            return super().form_valid(form)

class ServiceUpdate (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Services
    template_name = 'Hairapp/service_update.html'
    fields = ['name', 'price']

    def test_func(self):
        salon = self.get_object()
        if self.request.user == salon.salon:
            return True
        return False

    def form_valid(self, form):
            form.instance.salon = self.request.user
            messages.info(self.request, 'Salon Updated successfully')
            return super().form_valid(form)


class SalonDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HairSalon
    success_url = '/home'

    def test_func(self):
        salon = self.get_object()
        self.request.user.userpage.status = 'CUSTOMER'
        if self.request.user == salon.salon:
            return True
        return False


def yoursalon(request):
    if request.user.userpage.status == 'HOST':
        salon = HairSalon.objects.filter(salon=request.user).first()
        reservations = Reservations.objects.filter(host = request.user.hairsalon)
        customers = len(reservations)
        services = Services.objects.filter(name = request.user.hairsalon)
        context = {
            'salon': salon, 'customers':customers, 'services':services
        }
        return render(request, 'yoursalon.html', context)
    else:
        messages.info(request, 'You are not a HOST')
        return redirect('/home')

@login_required
def reservations(request):
    salon = HairSalon.objects.filter(salon=request.user).first()
    reservations = Reservations.objects.filter(host = salon)
    context = {
        'reservations':reservations, 'salon':salon
    }
    return render(request, 'Hairapp/reservations.html', context)


# class GetReservation(LoginRequiredMixin, ListView):
#     model = Reservations
#     template_name = 'reservations.html'
#     context_object_name = 'reservations'
#     ordering = ['date_created']

#     def get_queryset(self):
#         name = get_object_or_404(HairSalon, salon = self.kwargs.get('salon') )
#         return Reservations.objects.filter(host = name)


# class SalonReserve (LoginRequiredMixin, UpdateView):
#     model = HairSalon
#     template_name = 'Hairapp/hairsalon_detail.html'

#     def form_valid(self, form):
#             form.instance.salon = self.request.user
#             messages.info(self.request, 'Salon Updated successfully')
    
    
    
    #         return super().form_valid(form)

# def reserver(request):
#         name = request.user.username
#         salon = HairSalon.objects.filter(id = id).first()
#         salon.customer_queue += 1
#         salon.Reservation.append(", " + name)
#         salon.save(update_fields = ['customer_queue','Reservation'])
#         messages.success(request, "You have successfully reserved a seat")
#         return redirect('/home')

# @login_required
# def openess(request):
#     salon = HairSalon.objects.filter(salon=request.user).first()

#     if salon.is_open == 'OPENED':
#         HairSalon.objects.filter(salon=request.user).first().update(is_open = 'CLOSED')
#         return redirect('/yoursalon')
#     else:            
#         HairSalon.objects.filter(salon=request.user).first().is_open(is_open = 'OPENED')
#         return redirect('/yoursalon')


# class SalonCreate(LoginRequiredMixin ,CreateView):
#     model = HairSalon
#     fields = ['location','Available_services_list','salon_image']

#     def to_list(self):
#         Id = self.salon.id
#         services = HairSalon.objects.get(id = Id).Available_services
#         services_list = services.split(',')
#         for service in services_list:
#             services_list.append((service,service))
#         self.Services = services_list
#         return self.Available_services

#     def form_valid(self, form):
#         form.instance.salon = self.request.user
#         return super().form_valid(form)