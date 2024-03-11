from django.core import paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .models import *

paginator



class SubstationsView(generic.ListView):
    model = Substation
    template_name = "substation/all.html"
    context_object_name = "substations"
    paginate_by = 10


class SubstationView(generic.DetailView):
    model = Substation
    template_name = "substation/all.html"
    context_object_name = "substations"



def get_substation_for_id(request, tp: int) -> HttpResponse:
    try:
        tp = Substation.objects.get(pk=tp)
    except Substation.DoesNotExist:
        return redirect('substation:all_url')
    context = {'substation': tp}
    return render(request, 'substation/get_one.html', context)


def search_by_args(request, city, view=None, number=None):
    print(city, view, number)
    w = Substation.objects.all()[1]
    print(w.city.name_transle)
    if number:
        try:
            tp = Substation.objects.get(city=city, view=view, number=number)
            print(True)
        except Substation.DoesNotExist:
            return redirect('substation:all_url')
        return render(request, 'substation/get_one.html', {'substation': tp})

    try:
        tp = Substation.objects.get(pk=1)
    except Substation.DoesNotExist:
        return redirect('substation:all_url')
    context = {'substation': tp}
    return render(request, 'substation/get_one.html', context)
