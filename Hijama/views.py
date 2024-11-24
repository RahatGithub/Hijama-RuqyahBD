from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'Hijama/index.html') 

# class Services(View):
#     def get(self, request):
#         return render(request, 'Hijama/services.html')