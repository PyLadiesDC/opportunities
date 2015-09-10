import factory

from factory.fuzzy import FuzzyChoice

from opportunities_app.models import Post


class PostFactory(factory.django.DjangoModelFactory):

  archived = False
  email = 'email@example.org'
  point_of_contact = 'John Doe'

  name = factory.Sequence(lambda n: 'Test Job Posting {0}'.format(n))
  organization_name = factory.Sequence(lambda n: 'Company {0}'.format(n))
  is_compensated = True
  compensation = 50
  content = 'This is some content for a job posting.'
  benefits = 'Here are some additional things.'

  class Meta:
    model = Post

