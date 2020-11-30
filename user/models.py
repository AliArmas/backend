from django.db import models

class User():
    id = models.AutoField(primary_key = True)
    user = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 10)
    status = models.BooleanField()
    
    def __str__(self): 
        return self.name
