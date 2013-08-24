from django import forms
from django.forms import ModelForm
from peddlr.models import Checkin, Item
from geoposition.fields import GeopositionField


class CheckinForm(ModelForm):
    # expiry_offset = forms.CharField(label='For how long?')
    latitude = forms.CharField(widget=forms.HiddenInput())
    longitude = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Checkin
        exclude = ('expiry', 'point')

ITEM_CHOICES = Item.objects.all()

ITEM_CHOICES = (
    ("visa", "Visa"),
    ("mastercard", "MasterCard"),
)


class BuyerSearchForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple)
    latitude = forms.CharField(widget=forms.HiddenInput())
    longitude = forms.CharField(widget=forms.HiddenInput())
