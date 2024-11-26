from django.urls import path 
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('assessment/', Assessment.as_view(), name='assessment'),
]