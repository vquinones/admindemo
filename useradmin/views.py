from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
#from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns
from django.contrib import admin


class ScreenConfigurationView(TemplateView):
    template_name = 'admin/content/screen.configuration.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ScreenConfigurationView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScreenConfigurationView, self).dispatch(*args, **kwargs)


class DisplayConfigurationView(TemplateView):
    template_name = 'admin/content/display.configuration.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DisplayConfigurationView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DisplayConfigurationView, self).dispatch(*args, **kwargs)


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^my_view/$', admin.site.admin_view(ScreenConfigurationView.as_view()))
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls