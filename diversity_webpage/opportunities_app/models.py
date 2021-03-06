from django.db import models
from django.db.models.signals import pre_save

from opportunities_app.utils import create_token, ensure_token_uniqueness


class Post(models.Model):
  """
  A job posting.
  """

  ''' Types of salary compensation '''
  COMPENSATION_TYPES = (
    ('h', 'Hourly'),
    ('s', 'Salary')
  )

  token = models.CharField(max_length=100, unique=True)

  archived = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  email = models.EmailField()
  address = models.CharField(max_length=100, blank=True, null=True,
    help_text='Address of the business')
  point_of_contact = models.CharField(max_length=100,
    help_text='Person to contact')

  name = models.CharField(max_length=100, help_text='Title of the job post')
  organization_name = models.CharField(max_length=100, blank=True, null=True,
    help_text='Name of company or organization')
  is_compensated = models.BooleanField(help_text="Is this opportunity paid?", default=False)
  compensation = models.TextField(help_text="What is the pay?", blank=True, null=True)
  content = models.TextField(help_text='What is the job description?')
  benefits = models.TextField(help_text='What are the benefits this opportunity\
    provides.', blank=True, null=True)

  expiration = models.DateTimeField(blank=True, null=True,
    help_text='Expiration date of posting')
  filled_opportunity = models.BooleanField(default=False,
    help_text='Was this opportunity filled?')

  def __unicode__(self):
    return self.name if self.name else None

  def refresh_token(self):
    new_token = create_token()
    while not ensure_token_uniqueness(new_token):
        new_token = create_token()
    self.token = new_token


def create_token_on_new_post(sender, instance, **kwargs):
    """
    New posts won't have tokens. We refresh their token.
    """
    if instance.token == '':
        instance.refresh_token()


pre_save.connect(create_token_on_new_post, sender=Post,
    dispatch_uid='Token_on_creation')

