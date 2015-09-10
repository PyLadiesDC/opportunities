from django.db import models
from django.db.models.signals import pre_save

from opportunities_app.utils import create_token, ensure_token_uniqueness

"""
# Workflow:
## Job posting creation
User requests token for job post creation and provides email
User receives email
User uses email link to get to website to update and create


## Recovery:
User browses to specific job
Requests token refresh
See job posting creation workflow

"""

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
  compensation_type = models.CharField(max_length=1, choices=COMPENSATION_TYPES,
    help_text='Type of compensation')
  compensation_amount = models.CharField(max_length=50,
    help_text='Dollars/time period')
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
    import ipdb; ipdb.set_trace()
    if kwargs['created']:
        instance.refresh_token()


pre_save.connect(create_token_on_new_post, sender=Post,
    dispatch_uid='Token_on_creation')

