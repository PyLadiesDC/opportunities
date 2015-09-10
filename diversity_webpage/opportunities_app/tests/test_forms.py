from django.test import TestCase
from django.core import mail

from opportunities_app.forms import EmailForm, InvalidMailError
from opportunities_app.factories import PostFactory

class TestPostSubmissionForm(TestCase):
  def setUp(self):
    self.post = PostFactory()

  def test_form_valid_submission_email(self):
    data = {
      'name': 'Jane Doe',
      'email': 'example@example.com',
      'email_text': 'Hello world.'
    }
    email_form = EmailForm(data=data)
    assert email_form.is_valid()

    email_form.send_mail(self.post)
    assert len(mail.outbox) > 0

  def test_form_invalid_failure(self):
    data = {
        'name': None,
        'email': None,
        'email_text': None
    }
    email_form = EmailForm(data=data)
    assert not email_form.is_valid()

    with self.assertRaises(InvalidMailError):
        email_form.send_mail(self.post)
    assert len(mail.outbox) == 0

  def tearDown(self):
    pass
