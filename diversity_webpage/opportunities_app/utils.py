import binascii
import os


def create_token(n=70):
  """
  Creates a new token that is hopefully unique.
  """
  return binascii.hexlify(os.urandom(n))


def ensure_token_uniqueness(new_token):
  """
  Checks to see if the token is unique against existing tokens in the
  database.
  Returns False if the token exists, True otherwise.
  """
  from opportunities_app.models import Post
  return False if Post.objects.filter(token=new_token).exists() else True

