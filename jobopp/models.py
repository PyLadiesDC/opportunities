from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    poc = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
	self.published_date = timezone.now()
	self.save()

def __str__(self):
	return self.name

def __str__(self):
	return self.address

def __str__(self):
	return self.city
    
def __str__(self):
  return self.state

def __str__(self):
	return self.poc

def __str__(self):
	return self.email

def __str__(self):
  return self.phone      

def __str__(self):
  return self.term

def __str__(self):
  return self.salary

def __str__(self):
  return self.email

def __str__(self):
  return self.skills

def __str__(self):
  return self.description