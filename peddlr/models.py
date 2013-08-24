from django.db import models
from geoposition.fields import GeopositionField


class Checkin(models.Model):
    seller_name = models.CharField(max_length=255)
    location = GeopositionField()
    items = models.ManyToManyField(Items,)
    time = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField(help_text=u'Seconds')


class Items(models.Model):
    name = models.CharField(max_length=255, )


class CheckinItem(models.Model):
    price = models.CharField(max_length=100, )
    unit = models.CharField(max_length=55, help_text=u'Per lb or per item')
    item = models.ForeignKey(Items,)
    checkin = models.ForeignKey(Checkin,)

