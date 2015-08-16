from django.db import models

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	point_of_contact = models.CharField(max_length=100)
	phone = models.IntegerField(default=0)
	email = models.CharField(max_length=100)
	content = models.TextField()

	def __unicode__(self):
		return self.title
	
# Its the shape of the data as it is going into the database, and coming from the databse . that is a model. 
