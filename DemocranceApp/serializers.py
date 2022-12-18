from rest_framework import serializers

from .models import Customer, Policy

class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customer
       fields = ('first_name', 'last_name', 'dob')
       

class PolicySerializer(serializers.ModelSerializer):
   class Meta:
       model = Policy
       fields = ('type', 'premium', 'cover', 'state', 'customer_id')

        # "type": "personal-accident",
        #     "premium": "200.00",
        #     "cover": "200000.00",
        #     "state": "New",
        #     "cid": 1
