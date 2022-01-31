from .models import City,View,Substation

import random


city_list = [
        'Усолье сибирское',
        'Белоречинск',
        'Мальта',
        'Тельма',
        ]

view_list = [
        'ТП',
        'ГПП',
        'РП',
        'ГРУ',
        'ВРУ'
        ]

number_list = [i for i in range(100)]


def init_city():
    for i in city_list:
        City.objects.create(name=i)
    [print(i) for i in City.objects.all()]



def init_view():
    for i in view_list:
        View.objects.create(name=i)
    [print(i) for i in View.objects.all()]


def init_sub():
    for _ in range(100):
        c = random.choice(City.objects.all())
        v = random.choice(View.objects.all())
        n = random.choice(number_list)
        Substation.objects.create(city=c, view=v, number=n)
    [print(i) for i in Substation.objects.all()]

