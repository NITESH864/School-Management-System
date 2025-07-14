from django.db import models

# Create your models here.
class Enquiry(models.Model):
    # name=models.CharField(max_length=50)
    # gender=models.CharField(max_length=10)
    # address=models.TextField()
    # Contactno=models.CharField(max_length=15)
    # email=models.CharField(max_length=50)
    # enquirytext=models.TextField()
    # enquirydate=models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)    
    Contactno=models.CharField(max_length=15)
    enquirytext=models.TextField()

class AdminLogin(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    