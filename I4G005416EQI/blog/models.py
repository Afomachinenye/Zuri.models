from django.db import models
from django.db import models
import datetime
# Create your models here. 

class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Created_date =  models.DateTimeField()
    Published_date =  models.DateTimeField()

