from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
   ]
