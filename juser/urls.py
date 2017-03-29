from django.conf.urls import patterns, include, url
from jumpserver.api import view_splitter
from juser.views import *

urlpatterns = patterns('rightapply.views',
                       url(r'^apply/list/$', 'apply_list', name='app_list'),
                       url(r'^apply/add/$', 'apply_add', name='app_add'),
                       url(r'^apply/add_by_gpqx/$', 'add_by_gpqx', name='add_by_gpqx'),
                       url(r'^apply/check_list/$', 'check_list', name='check_list'),
                       url(r'^apply/check_app/$', 'check_app', name='check_app'),
                       url(r'^apply/follow/$', 'follow_app', name='follow_app'),
                       url(r'^apply/app_detail/$', 'app_detail', name='app_detail'),
                       url(r'^apply/del/$', 'apply_del', name='app_del'),
                       url(r'^apply/rule_list/$', 'app_rule_list', name='app_rule_list'),
                       url(r'^apply/rule_detail/$', 'app_rule_detail', name='app_rule_detail'),
                       )
