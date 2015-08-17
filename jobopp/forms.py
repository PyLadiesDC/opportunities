from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','name','address','city','state','poc', 'email','phone', 'term','salary','skills', 'description',)