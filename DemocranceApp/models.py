from django.db import models

#The database Schema / Model 

#Customer Class
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dob = models.DateField()

#Policy_State Class - Not used for now
class Policy_State(models.Model):
    state_name = models.CharField(max_length=50)

#Policy_Type Class - Not used for now
class Policy_Type(models.Model):
    type_name = models.CharField(max_length=50)

#Policy Class - Foreign Keys should be added in the future - avoided for now to simplify the development process matching the example needed in the test
class Policy(models.Model):
    quote_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    premium = models.DecimalField(max_digits=6, decimal_places=2, default= 100.00)
    cover = models.DecimalField(max_digits=9, decimal_places=2, default= 100000.00)
    state = models.CharField(max_length=50, default="New")
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #sid = models.ForeignKey(Policy_State, on_delete=models.CASCADE)
    #tid = models.ForeignKey(Policy_Type, on_delete=models.CASCADE)

#Policy_History Class to keep history and changes for all Policies
class Policy_History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ph_pid = models.ForeignKey(Policy, on_delete=models.CASCADE)
    ph_state = models.CharField(max_length=50)