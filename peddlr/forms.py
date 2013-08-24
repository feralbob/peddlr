from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from peddlr.models import Checkin, Item, CheckinItem
from geoposition.fields import GeopositionField


class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ['seller_name', 'location']

# CheckinItemFormSet = inlineformset_factory(Checkin, CheckinItem, form=CheckinForm, extra=4)


class BuyerSearchForm(forms.Form):
    def __init__(self, items, *args, **kwargs):
        super(BuyerSearchForm, self).__init__(*args, **kwargs)
        self.fields['items'] = forms.CheckboxSelectMultiple(choices=[(i.id, str(name)) for name in items.all()], widget=forms.CheckboxSelectMultiple)

    location = GeopositionField()