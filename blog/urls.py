from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.redirect_home, name=' home '),
    url(r'^home/$', views.home, name=' home '),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name=' post_detail '),
    url(r'^post/new/$', views.post_new, name=' post_new '),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name=' post_edit '),
    url(r'^post/(?P<pk>[0-9]+)/comment/new/$', views.comment_new, name=' comment_new '),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    #html/css
    url(r'^htmlcss/$', views.htmlcss_home, name=' htmlcss_home '),

    #html examples
    url(r'^htmlcss/background_example/', views.background_example, name=' background_example '),
    url(r'^htmlcss/image_example/', views.image_example, name= ' image_example '),

    # C++
    url(r'^cpp/$', views.cpp_home, name=' cpp_home '),

    # Java
    url(r'^java/$', views.java_home, name=' java_home '),

    # C#
    url(r'^cs/$', views.cs_home, name=' cs_home '),

    # Python
    url(r'^py/$', views.py_home, name=' py_home '),


]

