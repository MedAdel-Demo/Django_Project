from django.forms import ModelForm
from django import forms
from .models import Customer, Policy
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'dob']

    def clean(self):
        super(CustomerForm, self).clean()
        
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        dob = self.cleaned_data['dob']
        
        if  not Customer.objects.filter(first_name=first_name).filter(last_name=last_name).filter(dob=dob).exists():
            raise ValidationError ('Invalid Customer Details')
        
        self.cleaned_data['customer_id'] = Customer.objects.filter(first_name=first_name).filter(last_name=last_name).filter(dob=dob).first().pk
        return self.cleaned_data


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['type', 'premium', 'cover', 'state', 'customer_id']
