from django.db import models
from django. contrib. auth.models import AbstractUser

class Department(models.Model):  
    dep_id= models.AutoField(primary_key=True,verbose_name="Depid")
    department=models.CharField(max_length=100,verbose_name="Department")
    def __str__(self):
        return self.department
    class Meta:  
        db_table = "Department" 

class User(AbstractUser):  
    name=models.CharField(max_length=100,verbose_name="Name")
    address=models.CharField(max_length=100,verbose_name="Address")
    phoneno=models.IntegerField(verbose_name="Phone")
    email=models.EmailField(verbose_name="Email")
    age=models.IntegerField(verbose_name="age")
    qualification=models.CharField(max_length=100,verbose_name="Qualification")
    djoin=models.DateField(verbose_name="Joining Date")
    dep_id = models.ForeignKey(Department, on_delete = models.CASCADE)
    status=models.IntegerField(verbose_name="Status", default='0')
    class Meta:  
        db_table = "Usertable" 


 

