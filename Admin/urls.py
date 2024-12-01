from django.urls import path 
from .views import *

urlpatterns = [
    # path('dashboard/', DashboardView.as_view(), name='user_dashboard'),
    
    # user/client related paths
    path('users/', UserListView.as_view(), name='view_all_users'),
    path('search-users/', UserSearchView.as_view(), name='search_users'),
    
    # appointment related paths
    path('appointments/', SelectiveAppointmentsView.as_view(), name='selective_appointments'),
    path('appointments/approve/', ApproveAppointmentView.as_view(), name='approve_appointment'),
    path('appointments/attend/', AttendAppointmentView.as_view(), name='attend_appointment'),
    path('appointments/cancel/', CancelAppointmentView.as_view(), name='cancel_appointment'),
    path('search-appointments/', AppointmentSearchView.as_view(), name='search_appointments'),
    
    # normal assessment related paths
    path('assessments/normal/', NormalAssessmentsView.as_view(), name='normal_assessments'),
    path('assessments/normal/<int:assessment_id>/', NormalAssessmentsView.as_view(), name='normal_assessments'),

    # hijama assessment related paths
    path('assessments/hijama/', HijamaAssessmentsView.as_view(), name='hijama_assessments'),
    path('assessments/hijama/<int:assessment_id>/', HijamaAssessmentsView.as_view(), name='hijama_assessments'),
    

    # ruqyah assessment related paths
    path('assessments/ruqyah/', RuqyahAssessmentsView.as_view(), name='ruqyah_assessments'),
    path('assessments/ruqyah/<int:assessment_id>/', RuqyahAssessmentsView.as_view(), name='ruqyah_assessments'),
    
    # counseling assessment related paths
    path('assessments/counseling/', CounselingAssessmentsView.as_view(), name='counseling_assessments'),
    path('assessments/counseling/<int:assessment_id>/', CounselingAssessmentsView.as_view(), name='counseling_assessments'),
]