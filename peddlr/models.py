from django.db import models
from geoposition.fields import GeopositionField


class Checkin(models.Model):
    seller_name = models.CharField(max_length=255)
    location = GeopositionField()
    time = models.DateTimeField(auto_now=True)
    expiry = models.IntegerField(help_text=u'Seconds', choices=((3600, u'1 Hour'),
                                                               (7200, u'2 Hours'),
                                                               (10800, u'3 Hours'),
                                                               (14400, u'4 Hours'),))


class Item(models.Model):
    name = models.CharField(max_length=255, )


class CheckinItem(models.Model):
    price = models.CharField(max_length=100)
    unit = models.CharField(max_length=55, help_text=u'Per lb or per item')
    item = models.ForeignKey(Item)
    checkin = models.ForeignKey(Checkin)
    options = models.CharField(max_length=255, choices=((0, u'Activity Level'), (1, u'Metric'),))

