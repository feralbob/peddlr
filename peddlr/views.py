from django.forms.models import inlineformset_factory
from django.shortcuts import render
from peddlr.forms import *
from peddlr.models import *
from django.forms.models import modelformset_factory

def home(request):

    return render(request, 'home.html', {})


def buy(request):

    form = BuyerSearchForm()

    checkin_list = Checkin.objects.all()

    return render(request, 'buy.html', {checkin_list: checkin_list, 'form': form})


def sell(request):
    form = CheckinForm()
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            form.save()

            # Redirect instead?
            # 'form': form,

    return render(request, 'sell.html', {'form': form})
