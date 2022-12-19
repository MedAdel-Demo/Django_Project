from rest_framework import serializers

from .models import Customer, Policy

#class created to serialize the Customer Model
class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customer
       fields = ('first_name', 'last_name', 'dob')
       
#class created to serialize the Policy Model
class PolicySerializer(serializers.ModelSerializer):
   class Meta:
       model = Policy
       fields = ('type', 'premium', 'cover', 'state', 'customer_id')
