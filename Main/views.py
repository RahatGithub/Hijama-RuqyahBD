from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'Main/index.html') 

class Services(View):
    def get(self, request):
        return render(request, 'Main/services.html')
    
class BookAppointment(View):
    def get(self, request):
        return render(request, 'Main/book_appointment.html')