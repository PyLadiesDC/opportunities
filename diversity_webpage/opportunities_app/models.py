from django.db import models


class Post(models.Model):
  """
  A job posting.
  """
  created_at = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  email = models.EmailField()
  address = models.CharField(max_length=100, blank=True, null=True,
    help_text='Address of the business')
  point_of_contact = models.CharField(max_length=100,
    help_text='Posting contact point')

  name = models.CharField(max_length=100, help_text='Title of the job post')
  content = models.TextField()

  def __unicode__(self):
    return self.title

# Its the shape of the data as it is going into the database, and coming from the databse . that is a model.

