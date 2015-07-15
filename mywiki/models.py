from django.db import models

# Create your models here.

class user(models.Model):
	userName = models.CharField(max_length=200)
	userEmail = models.CharField(max_length=200)
	userPassword = models.CharField(max_length=200)

class content(models.Model):
	contentTitle = models.CharField(max_length=200)
	userId = models.ForeignKey(user)
	content_text = models.CharField(max_length=200)
	date_added = models.DateTimeField('date added')

