from django.forms.models import inlineformset_factory
from django.shortcuts import render
from peddlr.forms import *
from peddlr.models import *


def home(request):

    return render(request, 'home.html', {})


def buy(request):

    # form = BuyerSearchForm()

    checkin_list = Checkin.objects.all()

    return render(request, 'buy.html', {checkin_list: checkin_list})


def sell(request):
    # form = CheckinItemFormSet
    form = CheckinForm

    return render(request, 'sell.html', {form: form})