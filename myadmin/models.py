from django.db import models

class Screen(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Screen'
        verbose_name_plural = 'Screens'