from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *


def main_menu(request):
    photo = Photo.objects.all()[:3]
    return render(request, 'tk/main_menu.html', {'photo': photo})


def test(request, *args, **kwargs):
    print(request, args, kwargs, sep='/n')
    return HttpResponse('Test')


class SubstationViewAll(ListView):
    model = Substation
    template = 'tk/substation/substation_all.html'

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, {self.model.__name__.lower(): obj})


def substation_view(request, **kwargs):
    substation = Substation.objects.all().filter(city=kwargs['city'], view=kwargs['view'], number=kwargs['number'])[0]
    return render(request, 'tk/substation/substation.html', {'substation': substation})


def filter_substation(request, **kwargs: str):
    if 'view' in kwargs:
        substation = Substation.objects.all().filter(city=kwargs['city'].lower(), view=kwargs['view'].lower())
    elif 'city' in kwargs:
        substation = Substation.objects.all().filter(city=kwargs['city'].lower())
    else:
        substation = Substation.objects.all()
    return render(request, 'tk/substation/substation_all.html', {'substation': substation})
