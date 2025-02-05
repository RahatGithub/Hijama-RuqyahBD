from django.urls import path 
from .views import *

urlpatterns = [
    # path('assessment/', Assessment.as_view(), name='assessment'),
    path('assessment/', create_assessment, name='assessment'),
]