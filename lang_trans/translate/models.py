from datetime import datetime
from django.db import models

# Create your models here.
class languagesModel(models.Model):
    name = models.TextField(max_length = 200)
    iso_code = models.TextField()
 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name

class votesModel(models.Model):
    type = models.CharField(max_length = 200)
    ip = models.TextField()
    date_time = models.DateTimeField()

 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.type