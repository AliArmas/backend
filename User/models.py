from django.db import models

class UserModel(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255,null=False)
    status = models.BooleanField(null=False)

    def __str__(self):
        return self.username    
