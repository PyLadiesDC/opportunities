from django import forms
from .models import JobPost

class PostForm(forms.ModelForm):
	
	class Meta:
		model = JobPost
		
		fields = ('company','email','job_id',
			'job_designation', 'job_description',
			'industry',)
