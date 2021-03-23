from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *


def main_menu(request):
    photo = Photo.objects.all()[:3]
    return render(request, 'tk/main_menu.html', {'photo': photo})


def test(request, *args, **kwargs):
    print(request)
    print(args, kwargs)
    return HttpResponse('Test')



class SubstationViewAll(ListView):
    model = Substation
    template = 'tk/substation/substation_all.html'
  



    def get(self, request):

        from unidecode import unidecode
        from django.template import defaultfilters
        slug = defaultfilters.slugify(unidecode('Паша плюшкин'))

        print(slug)
        obj = self.model.objects.all()
        return render(request, self.template, {self.model.__name__.lower(): obj})



def SubstationView(request, **kwargs):
    print(request)
    print(kwargs)
    return render(request, 'tk/substation/substation.html', {})





#class SubstationView(DetailView):
#    model = Substation
  #  template_name = 'tk/substation/substation.html'
#    context_object_name = 'substation'
