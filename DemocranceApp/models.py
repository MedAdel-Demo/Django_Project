from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dob = models.DateField()

class Policy_State(models.Model):
    state_name = models.CharField(max_length=50)

class Policy_Type(models.Model):
    type_name = models.CharField(max_length=50)

class Policy(models.Model):
    quote_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    premium = models.DecimalField(max_digits=6, decimal_places=2, default= 100.00)
    cover = models.DecimalField(max_digits=9, decimal_places=2, default= 100000.00)
    state = models.CharField(max_length=50, default="New")
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #sid = models.ForeignKey(Policy_State, on_delete=models.CASCADE)
    #tid = models.ForeignKey(Policy_Type, on_delete=models.CASCADE)

class Policy_History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ph_pid = models.ForeignKey(Policy, on_delete=models.CASCADE)
    ph_state = models.CharField(max_length=50)


""" Customer:-
id
first_name
last_name
dob

Policy:-
id
type
premium
cover
state
cid  reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

Policy_State
psid
state

Policy_Type
ptid
type

Policy_History
phid
pid
date
status """
