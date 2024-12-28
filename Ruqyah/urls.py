from django.urls import path 
from .views import *

urlpatterns = [
    path('assessment/', Assessment.as_view(), name='assessment'),
]