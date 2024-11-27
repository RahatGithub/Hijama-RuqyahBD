from django.shortcuts import render, redirect
from django.views import View
from .models import Assessment as HijamaAssessment
from Main.models import User

class Index(View):
    def get(self, request):
        return render(request, 'Hijama/index.html') 

class Assessment(View):
    def get(self, request):
        return render(request, 'Hijama/assessment.html')
    
    def post(self, request):
        user_id = int(request.POST.get('user'))
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        has_diabetes = request.POST.get('has-diabetes')
        blood_pressure = request.POST.get('blood-pressure')
        health_issues = request.POST.get('health-issues')

        # fetch the user
        user = User.objects.get(id=user_id)        

        # create new assessment
        assessment = HijamaAssessment(
            user=user, 
            age=age, 
            gender=gender, 
            has_diabetes=has_diabetes, 
            blood_pressure=blood_pressure, 
            health_issues=health_issues
        )
        assessment.save()

        return redirect(f'/book-appointment?user={user_id}&service={1}&assessment={assessment.id}')