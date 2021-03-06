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
    url(r'^htmlcss/frame_example1/', views.frame_example1, name=' frame_example1 '),
    url(r'^htmlcss/frame_example2/', views.frame_example2, name=' frame_example2 '),
    url(r'^htmlcss/frame_example3/', views.frame_example3, name=' frame_example3 '),

    # C++
    url(r'^cpp/$', views.cpp_home, name=' cpp_home '),

    # Java
    url(r'^java/$', views.java_home, name=' java_home '),

    # C#
    url(r'^cs/$', views.cs_home, name=' cs_home '),

    # Python
    url(r'^py/$', views.py_home, name=' py_home '),

    # JS Assignment
    url(r'^js/$', views.js_home, name=' js_home ')
]

