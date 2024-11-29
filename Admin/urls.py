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
    
    # assessment related paths
    path('assessments/normal/', NormalAssessmentsView.as_view(), name='normal_assessments'),
    path('assessments/hijama/', HijamaAssessmentsView.as_view(), name='hijama_assessments'),
    path('assessments/ruqyah/', RuqyahAssessmentsView.as_view(), name='ruqyah_assessments'),
    path('assessments/counseling/', CounselingAssessmentsView.as_view(), name='counseling_assessments'),
]