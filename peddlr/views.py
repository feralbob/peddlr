from django.shortcuts import render


def home(request):

    return render(request, 'home.html', {})


def buy(request):

    return render(request, 'buy.html', {})


def sell(request):

    return render(request, 'sell.html', {})