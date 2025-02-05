from django.db import models

# Models that inherit this, will have the below attributes/methods in common
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



class User(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    has_whatsapp = models.BooleanField(default=False)
    address = models.TextField(default='')


class Appointment(BaseModel):
    # Foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    
    # Non-negative integer for service (can use choices to represent different services)
    HIJAMA = 1
    RUQYAH = 2
    COUNSELING_LIVE = 31
    COUNSELING_ONLINE = 32
    SERVICE_CHOICES = [
        (HIJAMA, 'Hijama'),
        (RUQYAH, 'Ruqyah'),
        (COUNSELING_LIVE, 'Counseling Live'),
        (COUNSELING_ONLINE, 'Counseling Online'),
    ]
    service = models.IntegerField(choices=SERVICE_CHOICES)

    # Integer for status (can use choices to represent different statuses)
    PENDING = 0
    CONFIRMED = 1
    ATTENDED = 2
    CANCELLED = -1
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (ATTENDED, 'Closed'),
        (CANCELLED, 'Cancelled'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)

    # Date and time fields
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'Appointment #{self.id} for {self.user.name}'

    class Meta:
        ordering = ['-created_at', '-updated_at']  # Recent appointments appear first
