from django.test import TestCase

from opportunities_app.factories import PostFactory
from opportunities_app.utils import create_token, ensure_token_uniqueness


class TestTokenUtils(TestCase):
  def setUp(self):
    pass

  def test_basic_create_token(self):
    token = create_token()
    assert len(token)

  def test_create_token_custom_length(self):
    n = 50
    token = create_token(n)
    assert len(token) == n, "Token was not proper length. It was {0} when it should have been {1}".format(len(token), n)

  def test_create_token_fail_non_integer(self):
    with self.assertRaises(TypeError):
       token = create_token('80')

  def test_ensure_token_uniqueness(self):
    post = PostFactory()
    token = post.token
    assert not ensure_token_uniqueness(token), "Token was unique despite not being"

  def tearDown(self):
    pass

