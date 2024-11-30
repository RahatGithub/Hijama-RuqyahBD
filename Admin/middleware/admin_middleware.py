from django.shortcuts import render, redirect
from django.urls import reverse

class AdminRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the URL starts with '/admin/'
        if request.path.startswith('/admin/'):
            # Restrict access to superusers only
            if not request.user.is_superuser:
                return render(request, 'access_denied.html')  # Redirect to the error page

        # Allow the request to proceed for other URLs
        return self.get_response(request)