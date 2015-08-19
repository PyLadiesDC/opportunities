from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from opportunities_app.models import Post
from opportunities_app.forms import PostForm
# Create your views here.

def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	t = loader.get_template('opportunities_app/index_4.html')
	context_dict = {'latest_posts': latest_posts, }
	for post in latest_posts:
		post.url = post.name.replace(' ', '_')
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_url):
	single_post = get_object_or_404(Post, 
		name=post_url.replace('_', ' '))
	t = loader.get_template('opportunities_app/post_2.html')
	c = Context({'single_post' : single_post,})
	return HttpResponse(t.render(c))

#updating the app's view for handling the form logic (displaying form, saving data, alerting the user
	#about validation errors)
def add_post(request):
	context = RequestContext(request)
	#determine if request is GET or POST, if GET => display the post (line 39)
	#if POST, we are going to process the form data
	# if POST request we determine if the supplied data is valid or not
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid(): # is the form valid?
			form.save(commit=True) #yes? save to database via commit and redirect user to the index page
			return redirect(index)
		else:
			print form.errors #no? display errors to end user
	else:
		form = PostForm()
	return render_to_response('opportunities_app/add_post2.html', {'form' : form}, context)