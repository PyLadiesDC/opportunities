from django import forms
from opportunities_app.models import Post

from django.core.mail import send_mail

class InvalidMailError(Exception):
    pass

#we're creating a new modelForm thats mapped to our model via the Meta() inner class model=Post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'address', 'point_of_contact', 'organization_name', 'email', 'expiration', 'content',
                  'benefits', 'is_compensated', 'compensation']
        #each field has to have an associate column in the database


class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    email_text = forms.CharField(widget=forms.Textarea, label='Email/Application Text')

    def send_mail(self, post):
        if not self.is_valid():
            raise InvalidMailError('Your mail was not sent.')
        contact_email = post.email
        applicant_text = self.cleaned_data['email_text'] + '<br/></br>' + self.cleaned_data['name'] + "<br/>" + self.cleaned_data['email'] # Be sure applicant and email are sent to the contact

        send_mail('New Applicant from Opportunities!', applicant_text, 'from@example.com', [contact_email], fail_silently=False) #Send email to the contact!


