from django import forms
from django.forms import ModelForm
from peddlr.models import Checkin
from geoposition.fields import GeopositionField


class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ['items', 'seller_name', 'location']


class BuyerSearchForm(forms.Form):
    def __init__(self, items, *args, **kwargs):
        super(BuyerSearchForm, self).__init__(*args, **kwargs)
        self.fields['items'] = forms.CheckboxSelectMultiple(choices=[(i.id, str(name)) for name in items.all()], widget=forms.CheckboxSelectMultiple)

    location = GeopositionField()