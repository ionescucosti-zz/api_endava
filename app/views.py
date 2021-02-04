import datetime
import math
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from app.models import Requests


def index(request):

    return render(request, "index.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def power(request):
    base = int(request.GET.get('b', None))
    exponent = int(request.GET.get('e', None))

    if 'm' in request.GET.keys():
        modulus = int(request.GET.get('m', None))
        result = 'pow({}, {}, {}) = {}'.format(base, exponent, modulus, pow(int(base), int(exponent), int(modulus)))
        log = Requests(datetime.datetime.now(), 'fact', [base, exponent, modulus], result)
        log.save()
        return render(request, 'endpoint.html', {'result': result})

    result = 'pow({}, {}) = {}'.format(base, exponent, pow(int(base), int(exponent)))
    log = Requests(datetime.datetime.now(), 'fact', [base, exponent], result)
    log.save()
    return render(request, 'endpoint.html', {
        'result': result,
        'optional': 'Optionally can be added modulus parameter ex: m=2'
    })


def fib(request):
    n = int(request.GET.get('n', None))
    lst = []

    def fib(n):
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            yield a
            a, b = b, a + b
            counter += 1

    for x in fib(n - 1):
        lst.append(x)
    result = 'Element {} in Fibbonaci sequence is: {}'.format(n, lst[-1])
    log = Requests(datetime.datetime.now(), 'fib', n, result)
    log.save()
    return render(request, 'endpoint.html', {'result': result})


def fact(request):
    n = int(request.GET.get('n', None))
    result = 'factorial({}) = {}'.format(n, str(math.factorial(n)))
    log = Requests(datetime.datetime.now(), 'fact', n, result)
    log.save()
    return render(request, 'endpoint.html', {'result': result})
