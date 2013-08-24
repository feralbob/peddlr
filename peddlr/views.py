from django.shortcuts import render
from peddlr.forms import *
from django.contrib.gis.geos import fromstr
from peddlr.models import Checkin


def home(request):
    return render(request, 'home.html', {})


def buy(request):
    form = BuyerSearchForm()
    checkin_list = []
    if request.method == 'POST':
        form = BuyerSearchForm(request.POST)
        if form.is_valid():
            things = []
            for item in form.cleaned_data['items']:
                things.append(item.pk)
            point = fromstr("POINT(%s %s)" % (form.cleaned_data['longitude'], form.cleaned_data['latitude']))
            checkin_list = Checkin.objects.distance(point).order_by('distance').filter(items__in=things)
    return render(request, 'buy.html', {'checkin_list': checkin_list, 'form': form})


def sell(request):
    form = CheckinForm()
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.point = Point('%s %s') % (form.cleaned_data['longitude'], form.cleaned_data['latitude'])
            instance.point = fromstr("POINT(%s %s)" % (form.cleaned_data['longitude'], form.cleaned_data['latitude']))
            instance.save()
            # Redirect instead?
            # 'form': form,

    return render(request, 'sell.html', {'form': form})
