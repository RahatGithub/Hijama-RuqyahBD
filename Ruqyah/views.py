from django.shortcuts import render, redirect
from django.views import View
from .models import Assessment as RuqyahAssessment
from Main.models import User

class Index(View):
    def get(self, request):
        return render(request, 'Ruqyah/index.html') 

class Assessment(View):
    def get(self, request):
        return render(request, 'Ruqyah/assessment.html')
    
    def post(self, request):
        user_id = int(request.POST.get('user'))
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        has_diabetes = request.POST.get('has-diabetes')
        blood_pressure = request.POST.get('blood-pressure')
        health_issues = request.POST.get('health-issues')
        bad_dreams = request.POST.get('bad-dreams') == 'on'
        anxiety = request.POST.get('anxiety') == 'on'
        disappointment = request.POST.get('disappointment') == 'on'
        tension = request.POST.get('tension') == 'on'

        # fetch the user
        user = User.objects.get(id=user_id)        

        # create new assessment
        assessment = RuqyahAssessment(
            user=user, 
            age=age, 
            gender=gender, 
            has_diabetes=has_diabetes, 
            blood_pressure=blood_pressure, 
            health_issues=health_issues,
            bad_dreams=bad_dreams,
            anxiety=anxiety,
            disappointment=disappointment,
            tension=tension
        )
        assessment.save()

        return redirect(f'/book-appointment?user={user_id}&service={2}&assessment={assessment.id}')