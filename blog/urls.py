from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name=' home '),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name=' post_detail '),
    url(r'^post/new/$', views.post_new, name=' post_new '),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name=' post_edit '),

    # C++
    url(r'^cpp/$', views.cpp_home, name=' cpp_home '),

    # Internet Programming Assignment - List
    url(r'^exercise/$', views.exercise_home, name=' exercise_home '),

    # Internet Programming Assignment - Html files
    url(r'^exercise/exercise_1$', views.exercise_1, name=' exercise_1 '),

]

