from django.db import models


class Screens(models.Model):
    title = models.CharField(max_length=100)
    ##More fields here...

    def __unicode__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Screen'
        verbose_name_plural = 'Screens'


class Displays(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Displays'
        verbose_name_plural = 'Displays'