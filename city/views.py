from django.urls import reverse
from django.views import generic

from city import models, forms


# Create your views here.
class CityListView(generic.ListView):
    model = models.City
    template_name = "city/all.html"
    context_object_name = "citys"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('title')



class CityDetailView(generic.DetailView):
    model = models.City
    template_name = "city/one.html"
    context_object_name = "city"


class CityCreateView(generic.CreateView):
    model = models.City
    form_class = forms.CityForm
    template_name = "city/create.html"
    context_object_name = "city"


class CityUpdateView(generic.UpdateView):
    model = models.City
    form_class = forms.CityForm
    template_name = 'city/update.html'


class CityDeleteView(generic.DeleteView):
    model = models.City
    template_name = 'city/delete.html'
    context_object_name = "city"

    def get_success_url(self):
        return reverse('city:all_url')
