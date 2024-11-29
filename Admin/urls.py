from django.urls import path 
from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='user_dashboard'),
    # path('update-user/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('users/', UserListView.as_view(), name='view_all_users'),
    path('search-users/', UserSearchView.as_view(), name='search_users'),
    path('appointments/', SelectiveAppointmentsView.as_view(), name='selective_appointments'),

    path('appointments/approve/', ApproveAppointmentView.as_view(), name='approve_appointment'),
    path('appointments/attend/', AttendAppointmentView.as_view(), name='attend_appointment'),
    path('appointments/cancel/', CancelAppointmentView.as_view(), name='cancel_appointment'),
]