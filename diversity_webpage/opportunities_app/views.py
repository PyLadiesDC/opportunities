from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import ListView
from django.core.mail import send_mail

from opportunities_app.models import Post
from opportunities_app.forms import PostForm, EmailForm
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


class PostListView(ListView):
    template_name = 'opportunities_app/list_posts.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10


# Sends an email with application information to the email provided by the employer
def send_application(request, post_id):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            obj = Post.objects.get(pk=post_id)  #Queries database to get the employer information
            contact_email = obj.email  # Contact email
            applicant_name = form.name
            applicant_email = form.email
            applicant_text = form.email_text + '<br/></br>' + applicant_name + "<br/>" + applicant_email # Be sure applicant and email are sent to the contact
            send_mail('New Applicant from Opportunities!', applicant_text, 'from@example.com',
                [contact_email], fail_silently=False) #Send email to the contact!

        else:
            print form.errors
    else:
        form = EmailForm()

    return render(request, 'opportunities_app/email.html', {'form' : form, 'post_id': post_id})

