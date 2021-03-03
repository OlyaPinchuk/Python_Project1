import os
import json
from django.shortcuts import render


def do_action(request, **kwargs):
    int1 = kwargs['int1']
    symbol = kwargs['symbol']
    int2 = kwargs['int2']
    eq = f'{int1} {symbol} {int2}'
    res = None

    if symbol == '-':
        res = int1 - int2
    elif symbol == '+':
        res = int1 + int2
    elif symbol == '*':
        res = int1 * int2
    elif symbol == 'div':
        res = int1 / int2

    return render(request, 'calculator/calculator.html', {'eq': eq, 'res': res})