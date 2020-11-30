from django.db import models
from django.db.models.fields import CharField

class ClientModel(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255,null=False)
    status = models.BooleanField(null=False)

    def __str__(self):
        return self.username    