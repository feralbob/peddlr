from django import forms
from django.forms import ModelForm
from peddlr.models import Checkin, Item
from geoposition.fields import GeopositionField


class CheckinForm(ModelForm):
    # expiry_offset = forms.CharField(label='For how long?')

    class Meta:
        model = Checkin
        exclude = ('expiry',)


class BuyerSearchForm(forms.Form):
    def __init__(self, items, *args, **kwargs):
        super(BuyerSearchForm, self).__init__(*args, **kwargs)
        self.fields['items'] = forms.CheckboxSelectMultiple(choices=[(i.id, str(i)) for i in items.all()], widget=forms.CheckboxSelectMultiple)

    location = GeopositionField()