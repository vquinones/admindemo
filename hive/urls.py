from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from myadmin.views import ScreenConfigurationView, DisplayConfigurationView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/screen-configuration/(.*)', ScreenConfigurationView.as_view(), {}, name='screen_landing'),
    url(r'^admin/display-configuration/(.*)', DisplayConfigurationView.as_view(), {}, name='display_landing'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve', {
                                    'document_root': settings.MEDIA_ROOT}))