from django.shortcuts import render, redirect
from django.views import View
from .models import Assessment as CounselingAssessment
from Main.models import User

class Assessment(View):
    def get(self, request):
        return render(request, 'Counseling/assessment.html')
    
    def post(self, request):
        user_id = int(request.POST.get('user'))
        appointment_type = request.POST.get('appointment-type')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        reason = request.POST.get('reason')

        # calculate service code 
        if appointment_type == 'live': 
            service = 31
        elif appointment_type == 'online':
            service = 32 

        # fetch the user
        user = User.objects.get(id=user_id)        

        # create new assessment
        assessment = CounselingAssessment(
            user=user, 
            age=age, 
            gender=gender, 
            reason=reason
        )
        assessment.save()

        return redirect(f'/book-appointment?user={user_id}&service={service}&assessment={assessment.id}')