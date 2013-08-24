from django.db import models
from geoposition.fields import GeopositionField
from datetime import timedelta, datetime


class Item(models.Model):
    name = models.CharField(max_length=255, )

    def __unicode__(self):
        return self.name


class CheckinManager(models.Manager):
    def get_query_set(self):
        return super(CheckinManager, self).get_query_set().filter(expiry__gt=datetime.now())


class Checkin(models.Model):
    seller_name = models.CharField(max_length=255, verbose_name='Your name')
    location = GeopositionField()
    time = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField()
    expiry_offset = models.IntegerField(verbose_name='For how long?', default=3600, choices=( (3600, u'1 Hour'),
                                                                (7200, u'2 Hours'),
                                                                (10800, u'3 Hours'),
                                                                (14400, u'4 Hours'),))
    items = models.ManyToManyField(Item)
    notes = models.TextField(help_text='Any additional information you would like to share.')

    # objects = CheckinManager

    class Meta:
        ordering = ('-time',)

    def __unicode__(self):
        return self.seller_name

    def save(self, *args, **kwargs):
        self.expiry = datetime.now() + timedelta(0, self.expiry_offset)
        super(Checkin, self).save(*args, **kwargs)