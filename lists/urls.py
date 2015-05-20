from django.conf.urls import patterns, include, url
from lists import views as views

urlpatterns = patterns('',
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
)
