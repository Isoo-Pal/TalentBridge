from django import forms
from .models import Skills

class addSkills(forms.ModelForm):
    class Meta:
        model = Skills
        # fields = '__all__'
        # OR
        fields = [
            'title',
            'category',
            'description',
            'experience_level',
            'years_of_experience',
            'availability',
            'preferred_mode',
            'price_type'
        ]