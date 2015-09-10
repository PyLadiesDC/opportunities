from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import ListView

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



class PostFormView(FormView):
    form = EmailForm
    template_name = 'opportunities_app/email.html'

    def form_valid(self, form):
        post_id = self.request.GET['post_id']
        obj = get_object_or_404(Post, pk=post_id)
        form.send_mail(obj)
        return super(PostFormView, self).form_valid(form)

    def get_context_data(self, request, *args, **kwargs):
        ctx = super(PostFormView, self).get_context_data(request, *args, **kwargs)
        ctx['post_id'] = self.request.GET['post_id']
        return ctx
