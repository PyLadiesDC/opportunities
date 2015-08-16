from django.conf.urls import patterns, url
from opportunities_app import views

urlpatterns = patterns(
	'opportunities_app.views',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_id>\d+)/$', views.post, name='post'),
	url(r'^add_post/', views.add_post, name='add_post'), #add post form
	url(r'^(?P<post_url>\w+)/$', views.post, name ='post'),
)