from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=50,
                            null=False,
                            unique=True)


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)


class Tips(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_length=135)
