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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hijama_assessments')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='assessments', null=True, blank=True)
    age = models.IntegerField() 
    
    # Integer for gender (can use choices to represent different genders)
    MALE = 1
    FEMALE = 0
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES, default=MALE)

    # Integer for diabetes (can use choices to represent different status of diabetes)
    YES = 1
    NO = 0
    UNAWARE = -1
    DIABETES_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
        (UNAWARE, 'Unaware'),
    ]
    has_diabetes = models.IntegerField(choices=DIABETES_CHOICES, default=NO)

    # Integer for blood pressure (can use choices to represent different status of blood pressure)
    NORMAL = 0
    LOW = 1
    HIGH = 2
    UNAWARE = -1
    BLOODPRESSURE_CHOICES = [
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
        (HIGH, 'High'),
        (UNAWARE, 'Unaware'),
    ]
    blood_pressure = models.IntegerField(choices=BLOODPRESSURE_CHOICES, default=NORMAL)

    health_issues = models.TextField(default='')