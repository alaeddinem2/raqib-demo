
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# Create your models here.

class CustomerUser(AbstractUser):

    user_type_data=((1,"AdminUser"),(2,"AgentUser"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


class AdminUser(models.Model):

    id = models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomerUser,on_delete=models.CASCADE)
    name = models.CharField(null=True,blank=True,max_length=250)
    phone = models.CharField(null=True,blank=True,max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AgentUser(models.Model):

    id = models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomerUser,on_delete=models.CASCADE)
    name = models.CharField(null=True,blank=True,max_length=250)
    phone = models.CharField(null=True,blank=True,max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,blank=True,max_length=250)
    phone = models.CharField(null=True,blank=True,max_length=250)
    departement = models.CharField(null=True,blank=True,max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #    # return '/detail/{}'.format(self.pk)
    #    return reverse('detail',args=[self.pk])


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plateNumber = models.CharField(null=True,blank=True,max_length=250)
    name = models.CharField(null=True,blank=True,max_length=250)
    year = models.CharField(null=True,blank=True,max_length=250)
    driver = models.OneToOneField(Driver,on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class InOut(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.DO_NOTHING)
    in_out = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    objects = models.Manager()  


    def __str__(self):
        return self.vehicle.name  




@receiver(post_save,sender=CustomerUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(admin=instance)
        if instance.user_type == 2:
            AgentUser.objects.create(admin=instance)
        


@receiver(post_save,sender=CustomerUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.agentuser.save()
    