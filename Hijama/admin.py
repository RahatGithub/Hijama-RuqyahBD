from django.contrib import admin
from .models import *
from Main.models import User

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'appointment', 'age', 'gender', 'has_diabetes', 'blood_pressure', 'health_issues')

    # Custom method to display user ID and name
    def user_info(self, obj):
        return f"{obj.user.id} - {obj.user.name}"  # Replace `name` with the actual field for user's name

    user_info.short_description = "User"  # Column header name in the admin panel