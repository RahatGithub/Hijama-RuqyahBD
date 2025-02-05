from django.shortcuts import render, redirect
from django.views import View
from Main.models import User
from .models import Assessment as HijamaAssessment
from .forms import AssessmentForm


def create_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Replace 'success' with your success URL
    else:
        form = AssessmentForm()
    
    return render(request, 'Hijama/assessment.html', {'form': form})

# class Assessment(View):
#     def get(self, request):
#         return render(request, 'Hijama/assessment.html')
    
#     def post(self, request):
#         user_id = int(request.POST.get('user'))
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         has_diabetes = request.POST.get('has-diabetes')
#         blood_pressure = request.POST.get('blood-pressure')
#         health_issues = request.POST.get('health-issues')

#         form = AssessmentForm(request.POST)

#         # fetch the user
#         user = User.objects.get(id=user_id)        

#         # create new assessment
#         assessment = HijamaAssessment(
#             user=user, 
#             age=age, 
#             gender=gender, 
#             has_diabetes=has_diabetes, 
#             blood_pressure=blood_pressure, 
#             health_issues=health_issues
#         )
#         assessment.save()

#         return redirect(f'/book-appointment?user={user_id}&service={1}&assessment={assessment.id}')