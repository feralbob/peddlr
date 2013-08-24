from django import forms
from django.forms import ModelForm
from peddlr.models import Checkin
from geoposition.fields import GeopositionField


class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ['items', 'name', 'location']



class BuyerSearchForm(forms.Form):
    items = forms.DateField()
    location = GeopositionField()