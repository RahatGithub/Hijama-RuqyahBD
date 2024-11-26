from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address', 'has_whatsapp')
    search_fields = ('name', 'phone', 'address')
    list_filter = ('has_whatsapp',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'service', 'status', 'date', 'time')

    # Custom method to display user ID and name
    def user_info(self, obj):
        return f"{obj.user.id} - {obj.user.name}"  # Replace `name` with the actual field for user's name

    user_info.short_description = "User"  # Column header name in the admin panel