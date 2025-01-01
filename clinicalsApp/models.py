from django.db import models

# Create your models here.

class Patient(models.Model):
    
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age=models.IntegerField()
    
    
    
class ClinicalData(models.Model):
    COMPONENTS_NAME = [('hw','Height/Weight'),('bp','Blood Pressue'),('heartrate','Heart Rate'),]
    componentName=models.CharField(choices=COMPONENTS_NAME,max_length=20)
    componentValue = models.CharField(max_length=20)
    measureDateTime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    