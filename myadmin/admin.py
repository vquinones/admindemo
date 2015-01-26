from django.contrib import admin
from django.conf.urls import patterns, url
from django.template import RequestContext
from django.shortcuts import render_to_response
#Se pueden registar aqui los modelos necesarios para verlos en el custom admin view

from .models import Screen

class MyEntryAdmin(admin.ModelAdmin):
    review_template = 'admin/content/review.html'

    def get_urls(self):
        urls = super(MyEntryAdmin, self).get_urls()
        my_urls = patterns('',
            (r'\d+/review/$', self.admin_site.admin_view(self.review)),
        )
        return my_urls + urls

    def review(self, request, id):
        entry = Screen.objects.get(pk=id)

        return render_to_response(self.review_template, {
            'title': 'Review entry: %s' % entry.title,
            'entry': entry,
            'opts': self.model._meta,
            'root_path': self.admin_site.root_path,
        }, context_instance=RequestContext(request))

admin.site.register(Screen, MyEntryAdmin)

#admin.site.register(Screen)