from django.db import models
from Main.models import User, Appointment

# Models that inherit this, will have the below attributes/methods in common
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Assessment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments_user')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='assessments_appointment', null=True, blank=True)
    age = models.IntegerField() 
    
    # Integer for gender (can use choices to represent different genders)
    MALE = 1
    FEMALE = 0
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES, default=MALE)

    reason = models.TextField(default='') 
    comments = models.TextField(default='') 