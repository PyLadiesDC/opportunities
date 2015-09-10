from django import forms
from opportunities_app.models import Post


#we're creating a new modelForm thats mapped to our model via the Meta() inner class model=Post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'address', 'point_of_contact', 'organization_name', 'email', 'expiration', 'content',
                  'benefits', 'compensation_type', 'compensation_amount']
        #each field has to have an associate column in the database


class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    email_text = forms.CharField(widget=forms.Textarea, label='Email/Application Text')