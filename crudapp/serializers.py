from rest_framework import serializers
from .models import Customer
class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','first_name','last_name','email','mobile_number','data_store']