from .models import City, View, Substation

import random


class InitDataBase:
    def __init__(self):
        self.city_list = ['Усолье сибирское', 'Белоречинск', 'Мальта', 'Тельма', ]
        self.view_list = ['ТП', 'ГПП', 'РП']
        self.number_list = [i for i in range(100)]

    def init_city(self):
        for i in self.city_list:
            try:
                City.objects.create(title=i)
            except:
                pass
        [print(i) for i in City.objects.all()]

    def init_view(self):
        for i in self.view_list:
            try:
                View.objects.create(title=i)
            except:
                pass
        [print(i) for i in View.objects.all()]

    def init_sub(self):
        for _ in range(100):
            c = random.choice(City.objects.all())
            v = random.choice(View.objects.all())
            n = random.choice(self.number_list)
            Substation.objects.create(city=c, view=v, number=n)


    def run(self):
        self.init_city()
        self.init_view()
        self.init_sub()
