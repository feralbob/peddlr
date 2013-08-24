from django.forms.models import inlineformset_factory
from django.shortcuts import render
from peddlr.forms import *
from peddlr.models import *


def home(request):

    return render(request, 'home.html', {})


def buy(request):

    form = BuyerSearchForm()

    checkin_list = Checkin.objects.all()

    return render(request, 'buy.html', {checkin_list: checkin_list, 'form': form})


def sell(request):

    if request.method == 'POST':
        form = CheckinForm(request.POST)
        formset = CheckinItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            new_checkin = form.save()
            for form in formset:
                form.checkin = new_checkin
                form.save()



            return render(request, 'sell.html', {'form': form, 'formset': formset})
    else:
        form = CheckinForm()

    form = CheckinForm()
    formset = CheckinItemFormSet()


    return render(request, 'sell.html', {'form': form, 'formset': formset})
