import factory

from factory.fuzzy import FuzzyChoice

from opportunities_app.models import Post


class PostFactory(factory.django.DjangoModelFactory):

  archived = False
  email = 'email@example.org'
  point_of_contact = 'John Doe'

  name = factory.Sequence(lambda: 'Test Job Posting %n' % n)
  organization_name = factory.Sequence(lambda: 'Company %n' % n)
  compensation_type = FuzzyChoice(Post.COMPENSATION_TYPES)
  content = 'This is some content for a job posting.'
  benefits = 'Here are some additional things.'
  compensation_amount = '$50/hr'

  class Meta:
    model = Post

