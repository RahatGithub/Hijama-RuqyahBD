from django.shortcuts import render, redirect
from django.views import View
from .models import Assessment as UsualAssessment
from Main.models import User

class Index(View):
    def get(self, request):
        return render(request, 'Assessment/index.html') 

class Assessment(View):
    def get(self, request):
        return render(request, 'Assessment/assessment.html')
    
    def post(self, request):
        user_id = int(request.POST.get('user'))
        appointment_type = request.POST.get('appointment-type')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        reason = request.POST.get('reason')

        # calculate service code 
        if appointment_type == 'live': 
            service = 41
        elif appointment_type == 'online':
            service = 42 

        # fetch the user
        user = User.objects.get(id=user_id)        

        # create new assessment
        assessment = UsualAssessment(
            user=user, 
            age=age, 
            gender=gender, 
            reason=reason
        )
        assessment.save()

        return redirect(f'/book-appointment?user={user_id}&service={service}&assessment={assessment.id}')