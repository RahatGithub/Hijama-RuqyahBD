from django import forms
from .models import Assessment

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'  # Includes all fields from the model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.RadioSelect(),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your address'}),
            'diabetes': forms.RadioSelect(),
            'blood_pressure': forms.RadioSelect(),
            'current_treatment_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'বর্তমান চিকিৎসার বিবরণ দিন'}),
            'previous_treatment_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'পূর্ববর্তী চিকিৎসার বিবরণ দিন'}),
        }
