from django.db import models


# Create your models here.
class Teacher(models.Model):
    Name = models.CharField(max_length=80)
    Role = models.CharField(max_length=100, default='Assistant Teacher', 
                            choices=[('Senior Teacher','Senior Teacher'),
                                     ('Associate Teacher','Associate Teacher'),
                                     ('Assistant Teacher','Assistant Teacher'),
                                     ('Professor','Professor')
                                     ])
    Address = models.TextField()
    Phone = models.CharField(max_length=10)    
    

    def __str__(self):
        return self.Name