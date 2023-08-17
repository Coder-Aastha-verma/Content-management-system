from django.db import models

# Create your models here
class Footer(models.Model):
    name=models.CharField(max_length=15,blank=False)
    email=models.CharField(max_length=20,blank=False)
    hello=models.CharField(max_length=50,blank=False)
    def __str__(self):
        return  self.name
class Contact(models.Model):
    fname=models.CharField(max_length=15,blank=False)
    lname=models.CharField(max_length=50,blank=False)
    mail=models.CharField(max_length=50,blank=False)
    con_no=models.IntegerField(blank=False)
    mes_sage=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return  self.fname
class Blog(models.Model):
    title=models.CharField(max_length=25,blank=False)
    category=models.CharField(max_length=30,blank=False)
    Pic=models.ImageField(blank=True)
    des=models.CharField(max_length=30,blank=False)  
    def __str__(self):
        return self.title
class Login(models.Model):
    f_nm=models.CharField(max_length=30,blank=False)
    l_nm=models.CharField(max_length=30,blank=False)
    e_mai=models.CharField(max_length=10,blank=False)
    p_word=models.CharField(max_length=35,blank=False)
    def __str__(self):
        return self.f_name
class Signin(models.Model):
    f_nam=models.CharField(max_length=30,blank=False)
    l_nam=models.CharField(max_length=30,blank=False)
    e_ma=models.CharField(max_length=10,blank=False)
    pa_word=models.CharField(max_length=35,blank=False)
    p=models.CharField(max_length=35,blank=False)
    def __str__(self):
        return self.f_nam