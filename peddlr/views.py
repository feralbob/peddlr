from django.shortcuts import render
from peddlr.forms import *
from peddlr.models import *

def home(request):

    return render(request, 'home.html', {})


def buy(request):

    form = BuyerSearchForm()

    checkin_list = Checkin.objects.all()

    return render(request, 'buy.html', {form: form, checkin_list: checkin_list})


def sell(request):
    form = CheckinForm
    return render(request, 'sell.html', {form: form})