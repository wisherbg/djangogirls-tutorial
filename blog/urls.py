from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.post_list, name='post_list'),
  url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
  url(r'^post/new/$', views.add_new, name='add_new'),
  url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
  url(r'^drafts$', views.draft_posts, name='draft_posts'),
  url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
  url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
  url(r'^post/(?P<pk>\d+)/comment/$', views.post_comment, name='post_comment'),
  url(r'^comment/(?P<pk>\d+)/delete$', views.comment_delete, name='comment_delete'),
  url(r'^comment/(?P<pk>\d+)/approve$', views.comment_approve, name='comment_approve'),
]
