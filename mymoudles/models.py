from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    havemoney = models.BigIntegerField(blank=True,null=True)
    outmoney = models.BigIntegerField(blank=True,null=True)
    token = models.CharField(max_length=100, null=True)
    def findourmoney(self):
        pass

class income(models.Model):
    name = models.CharField(max_length=200)
    valu = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='income_user')

class debt(models.Model):
    name = models.CharField(max_length=200)
    allvalu = models.BigIntegerField()
    mounthvalu = models.BigIntegerField()
    finishtime = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='debt_user')

class outro(models.Model):
    name = models.CharField(max_length=200)
    valu = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='outro_user')
    fordebt = models.ForeignKey(debt,on_delete=models.CASCADE,related_name='outro_debt',blank=True,null=True)

class rootin(models.Model):
    name = models.CharField(max_length=200)
    allvalu = models.BigIntegerField()
    number = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rootin_user')
    income = models.ManyToManyField(income, related_name='income_outtro',blank=True,null=True)
    outro = models.ManyToManyField(outro, related_name='rootin_outtro', blank=True, null=True)

