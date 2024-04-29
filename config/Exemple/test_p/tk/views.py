from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *


def main_menu(request):
    photo = Photo.objects.all()[:3]
    return render(request, 'tk/main_menu.html', {'photo': photo})


def test(request, *args, **kwargs):
    s = '__'.join([f'{k}-{v}' for k, v in kwargs.items()])
    return HttpResponse(f'''{request.path}      ------{s}''')


# ---------Substation-------------------------------------------------------------------
class SubstationViewAll(ListView):
    model = Substation
    template = 'tk/work_temp/substation_all.html'

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, {self.model.__name__.lower(): obj})


def substation_view(request, **kwargs):
    substation = Substation.objects.all().filter(city=kwargs['city'], view=kwargs['substation_inside'], number=kwargs['number'])[0]
    return render(request, 'tk/work_temp/work_temp.html', {'work_temp': substation})


def filter_substation(request, **kwargs: str):
    substation = Substation.filter_substation_for_city_view(kwargs)
    if not substation:
        return redirect('tk:substation_all_url')
    return render(request, 'tk/work_temp/substation_all.html', {'work_temp': substation})

# --------------------------------------------------------------------------------------


# ---------------------------------Photo------------------------------------------------
class PhotoViewAll(ListView):
    model = Photo
    template = 'tk\photo\photo_all.html'

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, {self.model.__name__.lower(): obj})


def filter_photo(request, **kwargs: str):
    if 'year' in kwargs:
        substation = Photo.objects.all().filter(city=kwargs['city'].lower(), view=kwargs['substation_inside'].lower())
    elif 'month' in kwargs:
        substation = Photo.objects.all().filter(city=kwargs['city'].lower())
    elif 'day' in kwargs:
        substation = Photo.objects.all().filter(city=kwargs['city'].lower())
    else:
        return redirect('tk:substation_all_url')
    return render(request, 'tk/work_temp/substation_all.html', {'work_temp': substation})


def photo_view(request, **kwargs):
    substation = Photo.objects.all().filter(city=kwargs['city'], view=kwargs['substation_inside'], number=kwargs['number'])[0]
    return render(request, 'tk/work_temp/work_temp.html', {'work_temp': substation})