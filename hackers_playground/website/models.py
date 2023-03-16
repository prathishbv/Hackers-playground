from django.db import models
from django.contrib.auth.hashers import make_password
from django import forms

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email_id = models.EmailField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | {self.email_id}"
