from django.db import models


class Post(models.Model):
    """
    A job posting.
    """

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
    benefits = models.TextField(help_text='What are the benefits this opportunity provides?',
        blank=True, null=True)

    expiration = models.DateTimeField(blank=True, null=True,
        help_text='Expiration date of posting')
    filled_opportunity = models.BooleanField(default=False,
        help_text='Was this opportunity filled?')

    def __unicode__(self):
        return self.name if self.name else None
