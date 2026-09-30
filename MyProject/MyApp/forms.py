from django import forms
from .models import Pet


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet

        fields = [
            'pet_name',
            'pet_type',
            'age',
            'breed',
            'owner_name',
            'contact_number',
            'health_status',
        ]

        widgets = {

            'pet_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Buddy'
            }),

            'pet_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Dog'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 3'
            }),

            'breed': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Golden Retriever'
            }),

            'owner_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Juan Dela Cruz'
            }),

            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 09XXXXXXXXX'
            }),

            'health_status': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Healthy'
            }),
        }