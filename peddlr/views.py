from django.shortcuts import render
from peddlr.forms import *


def home(request):

    return render(request, 'home.html', {})


def buy(request):

    form = BuyerSearchForm()
    return render(request, 'buy.html', {form: form})


def sell(request):
    form = CheckinForm
    return render(request, 'sell.html', {form: form})