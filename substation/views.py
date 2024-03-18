from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import SubstationForm
from .models import Substation





class SubstationsListView(generic.ListView):
    model = Substation
    template_name = "substation/all.html"
    context_object_name = "substations"
    paginate_by = 10


class SubstationDetailView(generic.DetailView):
    model = Substation
    template_name = "substation/one.html"
    context_object_name = "work_temp"


class SubstationUpdateView(generic.UpdateView):
    model = Substation
    form_class = SubstationForm
    template_name = 'substation/update.html'

class SubstationDeleteView(generic.DeleteView):
    model = Substation
    template_name = 'substation/delete.html'
    success_url = '/'



def get_substation_for_id(request, tp: int) -> HttpResponse:
    try:
        tp = Substation.objects.get(pk=tp)
    except Substation.DoesNotExist:
        return redirect('work_temp:all_url')
    context = {'work_temp': tp}
    return render(request, 'work_temp/one.html', context)


def search_by_args(request, city, view=None, number=None):
    print(city, view, number)
    w = Substation.objects.all()[1]
    print(w.city.name_transle)
    if number:
        try:
            tp = Substation.objects.get(city=city, view=view, number=number)
            print(True)
        except Substation.DoesNotExist:
            return redirect('work_temp:all_url')
        return render(request, 'work_temp/one.html', {'work_temp': tp})

    try:
        tp = Substation.objects.get(pk=1)
    except Substation.DoesNotExist:
        return redirect('work_temp:all_url')
    context = {'work_temp': tp}
    return render(request, 'work_temp/one.html', context)
