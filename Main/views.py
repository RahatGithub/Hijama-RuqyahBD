from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Index(View):
    def get(self, request):
        return render(request, 'Main/index.html') 


class Services(View):
    def get(self, request):
        return render(request, 'Main/services.html')
    

class BookAppointment(View):
    def get(self, request):
        user_id = int(request.GET.get('user'))
        service = int(request.GET.get('service'))

        # fetch the user
        user = User.objects.get(id=user_id)        

        # create new appointment
        appointment = Appointment(user=user, service=service, status=0, date="2024-11-26", time="14:00:00")
        appointment.save() 

        return render(request, 'Main/appointment_request_success.html')


class UserInformation(View):
    def get(self, request):
        return render(request, 'Main/user_information.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        has_whatsapp = request.POST.get('has-whatsapp') == 'on'
        address = request.POST.get('address')
        service = request.POST.get('service')

        # Check if the user already exists
        user = User.objects.filter(name=name,phone=phone).first()

        # If the user does not exist, create a new one
        if not user:
            user = User(name=name, phone=phone, has_whatsapp=has_whatsapp, address=address)
            user.save()

        # Redirect with the user ID and other details
        return redirect(f'/{service}/assessment?user={user.id}')
