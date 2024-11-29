from django.views.generic import TemplateView, UpdateView, DeleteView, ListView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from Main.models import User, Appointment
from Assessment.models import Assessment as NormalAssessment
from Hijama.models import Assessment as HijamaAssessment
from Ruqyah.models import Assessment as RuqyahAssessment
from Counseling.models import Assessment as CounselingAssessment


# View All Users: Display all users on a separate page
class UserListView(ListView):
    model = User
    template_name = "Admin/users.html"
    context_object_name = "users"


# Search Users: Display search results based on query
class UserSearchView(ListView):
    model = User
    template_name = "search_results.html"
    context_object_name = "users"

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        return User.objects.filter(name__icontains=query) | User.objects.filter(phone__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query", "")
        return context

    

# List all upcoming or requested appointments (0: requested, 1: upcoming)
class SelectiveAppointmentsView(View):
    SERVICE_MAP = {
        1: "Hijama",
        2: "Ruqyah",
        31: "Counseling Live",
        32: "Counseling Online",
        41: "Assessment Live",
        42: "Assessment Online",
    }

    def get(self, request):
        url_query = request.GET.get('type')  # value of the 'type' query is passed with the url of the GET request
        if url_query == 'upcoming':
            data = Appointment.objects.filter(status=1).order_by('created_at')
            appointment_query_type = 'Upcoming'
        elif url_query == 'pending':
            data = Appointment.objects.filter(status=0).order_by('created_at')
            appointment_query_type = 'Pending'
        elif url_query == 'history':
            data = Appointment.objects.filter(status__in=[2, -1]).order_by('created_at')
            appointment_query_type = 'History of'

        # Make custom appointments object to be used in the template
        appointments = []
        for a in data:
            appointment = dict()
            appointment['id'] = a.id 
            appointment['user'] = a.user
            appointment['service'] = self.SERVICE_MAP.get(a.service)
            appointment['status'] = a.status
            appointment['date'] = a.date
            appointment['time'] = a.time 
            appointments.append(appointment)

        return render(request, 'Admin/selective_appointments.html', {'appointments': appointments, 'appointment_query_type': appointment_query_type, 'url_query': url_query})


class ApproveAppointmentView(View):
    def post(self, request):
        try:
            appointment_id = request.POST.get('appointment_id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.status = 1  # 1 means "approved" or "confirmed"
            appointment.save()
            url_query = request.POST.get('url_query')
            return redirect(f'/admin/appointments/?type={url_query}')  # SHOW A SUCCESS MESSAGE (TOAST/POPUP)
        except Appointment.DoesNotExist:
            return redirect(f'/admin/appointments/?type={url_query}')  # SHOW ERROR MESSAGE (TOAST/POPUP)


class AttendAppointmentView(View):
    def post(self, request):
        try:
            appointment_id = request.POST.get('appointment_id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.status = 2  # 2 means "attended"
            appointment.save()
            url_query = request.POST.get('url_query')
            return redirect(f'/admin/appointments/?type={url_query}')  # SHOW A SUCCESS MESSAGE (TOAST/POPUP)
        except Appointment.DoesNotExist:
            return redirect(f'/admin/appointments/?type={url_query}')  # SHOW ERROR MESSAGE (TOAST/POPUP)


class CancelAppointmentView(View):
    def post(self, request):
        try:
            appointment_id = request.POST.get('appointment_id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.status = -1  # -1 means "cancelled"
            appointment.save()
            url_query = request.POST.get('url_query')
            return redirect(f'/admin/appointments/?type={url_query}') # SHOW A SUCCESS MESSAGE (TOAST/POPUP)
        except Appointment.DoesNotExist:
            return redirect(f'/admin/appointments/?type={url_query}')  # SHOW ERROR MESSAGE (TOAST/POPUP)


# List all normal assessments
class NormalAssessmentsView(View):
    GENDER_MAP = {
        1: "Male",
        0: "Female",
    }

    def get(self, request):
        data = NormalAssessment.objects.all()

        # Make custom appointments object to be used in the template
        assessments = []
        for a in data:
            assessment = dict()
            assessment['id'] = a.id 
            assessment['user'] = a.user
            assessment['appointment'] = a.appointment
            assessment['age'] = a.age
            assessment['gender'] = self.GENDER_MAP.get(a.gender)
            assessment['reason'] = a.reason 
            assessment['comments'] = a.comments 
            assessments.append(assessment)

        return render(request, 'Admin/normal_assessment_data.html', {'assessments': assessments})
    

# List all hijama assessments
class HijamaAssessmentsView(View):
    GENDER_MAP = {
        1: "Male",
        0: "Female",
    }
    HAS_DIABETES_MAP = {
        1: "Yes",
        0: "No",
        -1: "Unaware"
    }
    BLOOD_PRESSURE_MAP = {
        0: "Normal",
        1: "Low",
        2: "High",
        -1: "Unaware"
    }

    def get(self, request):
        data = HijamaAssessment.objects.all()

        # Make custom appointments object to be used in the template
        assessments = []
        for a in data:
            assessment = dict()
            assessment['id'] = a.id 
            assessment['user'] = a.user
            assessment['appointment'] = a.appointment
            assessment['age'] = a.age
            assessment['gender'] = self.GENDER_MAP.get(a.gender)
            assessment['has_diabetes'] = self.HAS_DIABETES_MAP.get(a.has_diabetes)
            assessment['blood_pressure'] = self.BLOOD_PRESSURE_MAP.get(a.blood_pressure)
            assessment['health_issues'] = a.health_issues
            assessment['comments'] = a.comments 
            assessments.append(assessment)

        return render(request, 'Admin/hijama_assessment_data.html', {'assessments': assessments})
    
# List all ruqyah assessments
class RuqyahAssessmentsView(View):
    GENDER_MAP = {
        1: "Male",
        0: "Female",
    }
    HAS_DIABETES_MAP = {
        1: "Yes",
        0: "No",
        -1: "Unaware"
    }
    BLOOD_PRESSURE_MAP = {
        0: "Normal",
        1: "Low",
        2: "High",
        -1: "Unaware"
    }

    def get(self, request):
        data = RuqyahAssessment.objects.all()

        # Make custom appointments object to be used in the template
        assessments = []
        for a in data:
            assessment = dict()
            assessment['id'] = a.id 
            assessment['user'] = a.user
            assessment['appointment'] = a.appointment
            assessment['age'] = a.age
            assessment['gender'] = self.GENDER_MAP.get(a.gender)
            assessment['has_diabetes'] = self.HAS_DIABETES_MAP.get(a.has_diabetes)
            assessment['blood_pressure'] = self.BLOOD_PRESSURE_MAP.get(a.blood_pressure)
            assessment['health_issues'] = a.health_issues
            assessment['bad_dreams'] = a.bad_dreams
            assessment['anxiety'] = a.anxiety
            assessment['disappointment'] = a.disappointment
            assessment['tension'] = a.tension
            assessment['comments'] = a.comments 
            assessments.append(assessment)

        return render(request, 'Admin/ruqyah_assessment_data.html', {'assessments': assessments})
    

# List all counseling assessments
class CounselingAssessmentsView(View):
    GENDER_MAP = {
        1: "Male",
        0: "Female",
    }

    def get(self, request):
        data = CounselingAssessment.objects.all()

        # Make custom appointments object to be used in the template
        assessments = []
        for a in data:
            assessment = dict()
            assessment['id'] = a.id 
            assessment['user'] = a.user
            assessment['appointment'] = a.appointment
            assessment['age'] = a.age
            assessment['gender'] = self.GENDER_MAP.get(a.gender)
            assessment['reason'] = a.reason 
            assessment['comments'] = a.comments 
            assessments.append(assessment)

        return render(request, 'Admin/counseling_assessment_data.html', {'assessments': assessments})