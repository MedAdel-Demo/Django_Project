from rest_framework import serializers

from .models import Customer, Policy

class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customer
       fields = ('first_name', 'last_name', 'dob')


# class SpeciesSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Species
#        fields = ('name', 'classification', 'language')