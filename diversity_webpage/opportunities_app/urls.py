from django.conf.urls import patterns, url
from opportunities_app import views

urlpatterns = patterns(
    'opportunities_app.views',
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^add_post/', views.add_post, name='add_post'),
    url(r'^(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^apply/(?P<post_id>\d+)/$', views.PostFormView.as_view(), name='apply'),

)
