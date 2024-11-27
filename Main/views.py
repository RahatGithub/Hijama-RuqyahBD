from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from Hijama.models import Assessment as HijamaAssessment

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
        assessment_id = int(request.GET.get('assessment'))

        # fetch the user
        user = User.objects.get(id=user_id)        

        # create new appointment
        appointment = Appointment(user=user, service=service, status=0, date="2024-11-26", time="14:00:00")
        appointment.save() 

        if service == 1: #if the service is Hijama:
            assessment = HijamaAssessment.objects.get(id=assessment_id)
        # elif service == 2: #if the service is Ruqyah:
        #     assessment = RuqyahAssessment.objects.get(id=assessment_id)
        # elif service in [31, 32]: #if the service is Counseling:
        #     assessment = CounselingAssessment.objects.get(id=assessment_id)
        # elif service in [41, 42]: #if the service is Assessment:
        #     assessment = Assessment.objects.get(id=assessment_id)

        assessment.appointment = appointment
        assessment.save()

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
