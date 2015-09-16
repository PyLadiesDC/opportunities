from django.db import models
from django.utils import timezone

#Industries
INDUSTRIES = ( ('IT', 'IT'),
		('Healthcare', 'Healthcare'),
		('Finance', 'Medical'),
		('Retail','Retail'),
		('Media', 'Media'),
		('Food services', 'Food services'),
		('Other', 'Other'),
	     )


# Create your models here.
class JobPost(models.Model):
	company = models.CharField(max_length=200,default="Anonymous")
	email = models.EmailField()
	job_id = models.CharField(max_length=10,blank=False)
	job_designation = models.TextField(blank=False,max_length=500)
	industry = models.TextField(choices = INDUSTRIES, blank=False)
	job_description = models.CharField(max_length=200, blank=False)
	
	def __str__(self):
		return self.job_designation

