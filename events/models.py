from django.db import models

# Create your models here.

class Events(models.Model):
	event_name = models.CharField(max_length=250, null=True)
	date = models.DateField(null=True)
	time = models.TimeField(null=True)
	location = models.CharField(max_length=250, null=True)
	image = models.ImageField(upload_to='images/', null=True) 
	is_liked = models.BooleanField(default=False)