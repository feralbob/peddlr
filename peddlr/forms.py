from django import forms
from django.forms import ModelForm
from peddlr.models import Checkin, Item


class CheckinForm(ModelForm):
    latitude = forms.CharField(widget=forms.HiddenInput())
    longitude = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Checkin
        exclude = ('expiry', 'point', 'notes')


class BuyerSearchForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple)
    latitude = forms.CharField(widget=forms.HiddenInput())
    longitude = forms.CharField(widget=forms.HiddenInput())
