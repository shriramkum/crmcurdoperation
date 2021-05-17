from django.db import models

class Customer(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile_number=models.BigIntegerField()
    data_store=models.CharField(max_length=500)
