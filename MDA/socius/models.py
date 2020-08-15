from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from multi_email_field.fields import MultiEmailField
# Create your models here.
class Destination(models.Model):  
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics',default='destination_4.jpg')
    desc = models.TextField(default='Defualt Value')
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)

class UserList(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254,blank=True)
    coupon = models.CharField(max_length=100, blank=True, null=True)
    is_superuser = models.BooleanField(default=False,blank=True, null=True)


class memberdirectory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(default='Defualt Value')
    size = models.IntegerField(default=0)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='images')
    firstName = models.CharField(max_length=20,blank=True,default='')
    lastName = models.CharField(max_length=20,blank=True,default='')
    bio = models.TextField(default='', blank=True)
    tagLine = models.TextField(blank=True,default='')
    #profileStatus = models.IntegerField(default=0) #to know how much profile does the user completed
    status = models.TextField(blank=True,default='')

    def __str__(self):
        return self.user.username 

class contactInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emails = MultiEmailField()
    countryCode = models.IntegerField()
    phone = models.CharField(max_length=10, blank=True, default='')

    def __str__(self):
        return self.user.username

class address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flatNo = models.CharField(max_length=10,blank=True,default='')
    street = models.TextField(max_length=50,blank=True,default='')
    city = models.TextField(max_length=30,blank=True,default='')
    state = models.TextField(max_length=30,blank=True,default='')
    country = models.TextField(max_length=20,blank=True,default='')
    pinCode = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.user.username


class skills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill = models.TextField(blank=True,default='')
    speciality = models.TextField(blank=True,default='')

    def __str__(self):
        return self.user.username

class certificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True,default='')
    issuingOrg = models.TextField(blank=True,default='') #who issued the certificate
    issuedDate = models.DateField(null=True)
    expiryDate = models.DateField(blank=True)
    credentialId = models.TextField(blank=True,default='')
    credentialUrl = models.URLField(blank=True,default='')
    description = models.TextField(blank=True,default='')

    def __str__(self):
        return self.user.username

class testimonial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attestant = models.TextField(blank=True,default='') #the one who gives testimonial
    issuedDate = models.DateField(null=True) #should not be a future date---->need to be validated
    services = models.TextField(blank=True,default='') #product/services
    #no need to validate designation and location
    designation = models.TextField(blank=True,default='') 
    location = models.TextField(blank=True,default='')
    description = models.TextField(blank=True,default='')

    def __str__(self):
        return self.user.username

class education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.TextField(blank=True,default='')
    degree = models.CharField(max_length=50,blank=True,default='')
    branch = models.TextField(blank=True,default='')
    grade = models.FloatField()
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    description = models.TextField(blank=True,default='')

    def __str__(self):
        return self.user.username