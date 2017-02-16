from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^(?P<post_id>[0-9]+)/comment/add/$', views.comment_add, name='comment_add'),
    url(r'^(?P<post_id>[0-9]+)/like/toggle/$', views.post_like_toggle, name='like_toggle'),
]