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
    type = models.CharField(max_length=50)
    #tid = models.ForeignKey(Policy_Type, on_delete=models.CASCADE)
    premium = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.DecimalField(max_digits=9, decimal_places=2)
    sid = models.ForeignKey(Policy_State, on_delete=models.CASCADE)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Policy_History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ph_pid = models.ForeignKey(Policy, on_delete=models.CASCADE)
    ph_sid = models.ForeignKey(Policy_State, on_delete=models.CASCADE)


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
