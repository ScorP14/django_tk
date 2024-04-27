from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .forms import SubstationForm
from .models import Substation


class SubstationCreateView(generic.CreateView):
    model = Substation
    form_class = SubstationForm
    template_name = 'substation/create.html'


class SubstationsListView(generic.ListView):
    model = Substation
    template_name = "substation/all.html"
    context_object_name = "substations"
    paginate_by = 10


class SubstationDetailView(generic.DetailView):
    model = Substation
    template_name = "substation/one.html"
    context_object_name = "substation"


class SubstationUpdateView(generic.UpdateView):
    model = Substation
    form_class = SubstationForm
    template_name = 'substation/update.html'


class SubstationDeleteView(generic.DeleteView):
    model = Substation
    template_name = 'substation/delete.html'

    def get_success_url(self):
        return reverse('substation:all')


