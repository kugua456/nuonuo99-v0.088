#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('expert.views',
    url(r'^filter$', 'filter_html', name='expert_filter'),
)
