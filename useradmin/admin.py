from django.contrib import admin
from django.conf.urls import patterns, url
from django.template import RequestContext
from django.shortcuts import render_to_response
from sites import UserAdmin
from models import Screens, Displays


class ScreensAdmin(admin.ModelAdmin):
    #preview_template = 'admin/content/preview_scr.html' #small screen preview
    change_list_template = 'admin/content/screen_list.html'
    change_form_template = 'admin/content/screen_change.html'
    #add more configuration here

    def get_urls(self):
        urls = super(ScreensAdmin, self).get_urls()
        my_urls = patterns(
            '',
            #Add custom views for displaye here
            #(r'/rreview/', self.admin_site.admin_view(self.preview)),
        )
        return my_urls + urls


class DisplaysAdmin(admin.ModelAdmin):
    #preview_template = 'admin/content/review.html' #small display preview
    change_list_template = 'admin/content/display_list.html'
    change_form_template = 'admin/content/display_change.html'
    #add more configuration here


    ##More Options for model
    def get_urls(self):
        urls = super(DisplaysAdmin, self).get_urls()
        my_urls = patterns(
            '',
            #Add custom views for displaye here
            (r'/rreview/', self.admin_site.admin_view(self.preview)),
        )
        return my_urls + urls
    #
    def preview(self, request):
        entry = Displays.objects.get(pk=1)

        return render_to_response(self.preview_template,
        {
            'title': 'Review entry: %s' % entry.title,
            'entry': entry,
            'opts': self.model._meta,
        }, context_instance=RequestContext(request))




user_admin_site = UserAdmin(name='usersadmin')
user_admin_site.register(Screens, ScreensAdmin)
user_admin_site.register(Displays, DisplaysAdmin)