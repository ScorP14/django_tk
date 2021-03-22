from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *


def main_menu(request):
    photo = Photo.objects.all()[:3]
    return render(request, 'tk/main_menu.html', {'photo': photo})


def test(request):
    return HttpResponse('Test')



class SubstationViewAll(ListView):
    model = Substation
    template = 'tk/substation/substation_all.html'

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, {self.model.__name__.lower(): obj})


class SubstationView(DetailView):
    model = Substation
    template_name = 'tk/substation/substation.html'
    context_object_name = 'substation'
