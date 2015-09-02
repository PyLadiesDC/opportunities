from django.shortcuts import render, redirect
from .models import JobPost
from .forms import PostForm

# Create your views here.
def post_list(request):
	jobposts = JobPost.objects.all()
	return render(request, "myapp/post_list.html", {'jobposts': jobposts})

def post_new(request):
	if request.method=='POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('myapp.views.post_list')
			
	else:
		form = PostForm()
	return render(request, 'myapp/post_new.html',{'form':form})
	
