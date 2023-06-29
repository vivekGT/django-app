from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('client_admin', 'Client Admin'),
        ('tl', 'Team Leader'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=20, choices=USER_ROLES)
  


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
from django.db import models
from django.db.models import Q
from datetime import date

class Sample(models.Model):
    Model = models.CharField(max_length=255)
    DMS_Stock = models.IntegerField(db_column='DMS Stock')
    WS_TGT = models.IntegerField(db_column='WS TGT')
    WS_ACH = models.IntegerField(db_column='WS ACH')
    BAL_WS = models.IntegerField(db_column='BAL WS')
    Total_Probable_Stock = models.IntegerField(db_column='Total Probable Stock')

    date_created = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.Model

 

from django.db import models

class TeamLeaderData(models.Model):
    team_leader_name = models.CharField(max_length=100)
    team_leader_territory = models.CharField(max_length=100)
    per_day_asking = models.FloatField()
    enquiry_total = models.IntegerField(null=True)
    test_drive_percentage = models.IntegerField()
    home_visit_percentage = models.IntegerField()

    def __str__(self):
        return self.team_leader_name



from django.db import models

class salesEx(models.Model):
    mspin = models.IntegerField()
    dse_name = models.CharField(max_length=100)
    ageing = models.CharField(max_length=100)
    team_leader_name = models.CharField(max_length=100)
    unit_name = models.CharField(max_length=100)
    enquiry_total = models.IntegerField(null=True)
    test_drive = models.IntegerField()
    home_visit = models.IntegerField()

    def __str__(self):
        return self.dse_name 


        
    

    




