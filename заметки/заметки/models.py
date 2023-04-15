from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_lengh=50,
                            null=False,
                            unique=True)


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_lengh=15)


class Tips(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_leng=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_lengh=135)
