from django.forms import ModelForm
from django import forms
from .models import Customer
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'dob']

    def clean(self):
        super(CustomerForm, self).clean()
        
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if['Mohamed'] != first_name:
            raise ValidationError ('Name must contain Mohamed')
            return first_name

        return self.cleaned_data
