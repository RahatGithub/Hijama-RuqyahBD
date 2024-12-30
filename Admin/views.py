from django.views.generic import TemplateView, UpdateView, DeleteView, ListView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from Main.models import User, Appointment
from Hijama.models import Assessment as HijamaAssessment
from Ruqyah.models import Assessment as RuqyahAssessment
from Counseling.models import Assessment as CounselingAssessment
from django.contrib import messages
    


# View All Users: Display all users on a separate page
class UserListView(ListView):
    model = User
    template_name = "Admin/users.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the original context
        context = super().get_context_data(**kwargs)

        # Process the user instances
        custom_users = []
        for user in context["users"]:
            hijama_assessments = HijamaAssessment.objects.filter(user=user.id)
            ruqyah_assessments = RuqyahAssessment.objects.filter(user=user.id)
            counseling_assessments = CounselingAssessment.objects.filter(user=user.id)
            
            custom_users.append({
                "id": user.id,
                "name": user.name,
                "phone": user.phone,
                "has_whatsapp": user.has_whatsapp,
                "address": user.address,
                "normal_assessments": normal_assessments,
                "hijama_assessments": hijama_assessments,
                "ruqyah_assessments": ruqyah_assessments,
                "counseling_assessments": counseling_assessments
            })

        # Replace the users context with the processed users
        context["users"] = custom_users
        return context


# Search Users: Display search results based on query
class UserSearchView(ListView):
    model = User
    template_name = "Admin/user_search_results.html"
    context_object_name = "users"

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        return User.objects.filter(name__icontains=query) | User.objects.filter(phone__icontains=query) | User.objects.filter(address__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query", "")

        custom_users = []
        for user in context["users"]:
            hijama_assessments = HijamaAssessment.objects.filter(user=user.id)
            ruqyah_assessments = RuqyahAssessment.objects.filter(user=user.id)
            counseling_assessments = CounselingAssessment.objects.filter(user=user.id)
            
            custom_users.append({
                "id": user.id,
                "name": user.name,
                "phone": user.phone,
                "has_whatsapp": user.has_whatsapp,
                "address": user.address,
                "normal_assessments": normal_assessments,
                "hijama_assessments": hijama_assessments,
                "ruqyah_assessments": ruqyah_assessments,
                "counseling_assessments": counseling_assessments
            })

        context["users"] = custom_users
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
            data = Appointment.objects.filter(status__in=[2, -1]).order_by('-created_at')
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


# Search Appointments: Display search results based on query
class AppointmentSearchView(ListView):
    model = Appointment
    template_name = "Admin/appointment_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        return Appointment.objects.filter(user__name__icontains=query) | Appointment.objects.filter(user__phone__icontains=query) | Appointment.objects.filter(user__address__icontains=query)

    def get_context_data(self, **kwargs):
        # Base context data
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query", "")

        # Process custom appointment data
        raw_appointments = self.get_queryset()  # Raw queryset
        custom_appointments = []
        for appointment in raw_appointments:
            custom_appointments.append({
                "id": appointment.id,
                "user": appointment.user,
                "service": appointment.get_service_display(), # Uses service choices for display
                "status": appointment.get_status_display(),  # Uses status choices for display
                "date": appointment.date,
                "time": appointment.time,
            })

        # Add custom data to context
        context["appointments"] = custom_appointments
        context["query"] = query  # Include search query for template reference
        return context
    


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

    def get(self, request, assessment_id=None):
        if assessment_id is None:
            # List all assessments
            data = HijamaAssessment.objects.all()

            # Prepare custom assessments data for the template
            assessments = []
            for a in data:
                assessment = {
                    'id': a.id,
                    'user': a.user,
                    'appointment': a.appointment,
                    'age': a.age,
                    'gender': self.GENDER_MAP.get(a.gender),
                    'has_diabetes': self.HAS_DIABETES_MAP.get(a.has_diabetes),
                    'blood_pressure': self.BLOOD_PRESSURE_MAP.get(a.blood_pressure),
                    'health_issues': a.health_issues,
                    'comments': a.comments,
                    'submitted_on': a.created_at,
                }
                assessments.append(assessment)

            return render(request, 'Admin/hijama_assessment_data.html', {'assessments': assessments})

        else:
            # Show details of a specific assessment
            a = get_object_or_404(HijamaAssessment, id=assessment_id)
            assessment = {
                    'id': a.id,
                    'user': a.user,
                    'appointment': a.appointment,
                    'age': a.age,
                    'gender': self.GENDER_MAP.get(a.gender),
                    'has_diabetes': self.HAS_DIABETES_MAP.get(a.has_diabetes),
                    'blood_pressure': self.BLOOD_PRESSURE_MAP.get(a.blood_pressure),
                    'health_issues': a.health_issues,
                    'comments': a.comments,
                    'submitted_on': a.created_at,
                }
            return render(request, 'Admin/hijama_assessment_single_view.html', {'assessment': assessment})

    def post(self, request, assessment_id):
        # Update a specific assessment
        assessment = get_object_or_404(HijamaAssessment, id=assessment_id)

        # Get updated data from the form
        age = request.POST.get('age')
        has_diabetes = request.POST.get('has_diabetes')
        blood_pressure = request.POST.get('blood_pressure')
        health_issues = request.POST.get('health_issues', '').strip()
        comments = request.POST.get('comments', '').strip()

        # Update the record 
        assessment.age = age
        assessment.has_diabetes = has_diabetes
        assessment.blood_pressure = blood_pressure
        assessment.health_issues = health_issues
        assessment.comments = comments

        # Save the updated assessment
        assessment.save()
        messages.success(request, "Assessment updated successfully!")

        # Redirect back to the same assessment view
        return redirect('hijama_assessments', assessment_id=assessment.id)

    

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

    def get(self, request, assessment_id=None):
        if assessment_id is None:
            # List all assessments
            data = RuqyahAssessment.objects.all()

            # Prepare custom assessments data for the template
            assessments = []
            for a in data:
                assessment = {
                    'id': a.id,
                    'user': a.user,
                    'appointment': a.appointment,
                    'age': a.age,
                    'gender': self.GENDER_MAP.get(a.gender),
                    'has_diabetes': self.HAS_DIABETES_MAP.get(a.has_diabetes),
                    'blood_pressure': self.BLOOD_PRESSURE_MAP.get(a.blood_pressure),
                    'health_issues': a.health_issues,
                    'bad_dreams': a.bad_dreams,
                    'anxiety': a.anxiety,
                    'disappointment': a.disappointment,
                    'tension': a.tension,
                    'comments': a.comments,
                    'submitted_on': a.created_at,
                }
                assessments.append(assessment)

            return render(request, 'Admin/ruqyah_assessment_data.html', {'assessments': assessments})

        else:
            # Show details of a specific assessment
            a = get_object_or_404(RuqyahAssessment, id=assessment_id)
            assessment = {
                    'id': a.id,
                    'user': a.user,
                    'appointment': a.appointment,
                    'age': a.age,
                    'gender': self.GENDER_MAP.get(a.gender),
                    'has_diabetes': self.HAS_DIABETES_MAP.get(a.has_diabetes),
                    'blood_pressure': self.BLOOD_PRESSURE_MAP.get(a.blood_pressure),
                    'health_issues': a.health_issues,
                    'bad_dreams': a.bad_dreams,
                    'anxiety': a.anxiety,
                    'disappointment': a.disappointment,
                    'tension': a.tension,
                    'comments': a.comments,
                    'submitted_on': a.created_at,
                }
            return render(request, 'Admin/ruqyah_assessment_single_view.html', {'assessment': assessment})

    def post(self, request, assessment_id):
        # Update a specific assessment
        assessment = get_object_or_404(RuqyahAssessment, id=assessment_id)

        # Get updated data from the form
        age = request.POST.get('age')
        has_diabetes = request.POST.get('has_diabetes')
        blood_pressure = request.POST.get('blood_pressure')
        health_issues = request.POST.get('health_issues', '').strip()
        comments = request.POST.get('comments', '').strip()

        # Update the record 
        assessment.age = age
        assessment.has_diabetes = has_diabetes
        assessment.blood_pressure = blood_pressure
        assessment.health_issues = health_issues
        assessment.comments = comments

        # Save the updated assessment
        assessment.save()
        messages.success(request, "Assessment updated successfully!")

        # Redirect back to the same assessment view
        return redirect('ruqyah_assessments', assessment_id=assessment.id)
    
    


class CounselingAssessmentsView(View):
    GENDER_MAP = {
        1: "Male",
        0: "Female",
    }

    def get(self, request, assessment_id=None):
        if assessment_id is None:
            # List all assessments
            data = CounselingAssessment.objects.all()

            # Prepare custom assessments data for the template
            assessments = []
            for a in data:
                assessment = {
                    'id': a.id,
                    'user': a.user,
                    'appointment': a.appointment,
                    'age': a.age,
                    'gender': self.GENDER_MAP.get(a.gender),
                    'reason': a.reason,
                    'comments': a.comments,
                    'submitted_on': a.created_at,
                }
                assessments.append(assessment)

            return render(request, 'Admin/counseling_assessment_data.html', {'assessments': assessments})

        else:
            # Show details of a specific assessment
            a = get_object_or_404(CounselingAssessment, id=assessment_id)
            assessment = {
                    'id': a.id,
                    'user': a.user,
                    'appointment': a.appointment,
                    'age': a.age,
                    'gender': self.GENDER_MAP.get(a.gender),
                    'reason': a.reason,
                    'comments': a.comments,
                    'submitted_on': a.created_at,
                }
            return render(request, 'Admin/counseling_assessment_single_view.html', {'assessment': assessment})

    def post(self, request, assessment_id):
        # Update a specific assessment
        assessment = get_object_or_404(CounselingAssessment, id=assessment_id)

        # Get updated data from the form
        age = request.POST.get('age')
        reason = request.POST.get('reason', '').strip()
        comments = request.POST.get('comments', '').strip()

        # Update the record 
        assessment.age = age
        assessment.reason = reason
        assessment.comments = comments

        # Save the updated assessment
        assessment.save()
        messages.success(request, "Assessment updated successfully!")

        # Redirect back to the same assessment view
        return redirect('counseling_assessments', assessment_id=assessment.id)
