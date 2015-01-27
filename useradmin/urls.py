from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from useradmin.views import ScreenConfigurationView, DisplayConfigurationView
from useradmin.admin import user_admin_site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^screen-configuration/(.*)', ScreenConfigurationView.as_view(), {}, name='screen_landing'),
    url(r'^display-configuration/(.*)', DisplayConfigurationView.as_view(), {}, name='display_landing'),
)
