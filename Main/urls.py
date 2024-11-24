from django.urls import path 
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('services/', Services.as_view(), name='services'),
    path('book_appointment/', BookAppointment.as_view(), name='book_appointment'),
]