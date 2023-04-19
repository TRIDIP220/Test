from django.db import models

class User(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)


    class Meta:
        db_table ="User"



    
