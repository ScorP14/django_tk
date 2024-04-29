from django.urls import reverse
from django.views import generic


from substation_type import models, forms


class SubstationTypeListView(generic.ListView):
    model = models.SubstationType
    template_name = "substation_type/all.html"
    context_object_name = "substation_types"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('title')


class SubstationTypeDetailView(generic.DetailView):
    model = models.SubstationType
    template_name = "substation_type/one.html"
    context_object_name = "substation_type"


class SubstationTypeCreateView(generic.CreateView):
    model = models.SubstationType
    form_class = forms.SubstationTypeForm
    template_name = "substation_type/create.html"
    context_object_name = "substation_type"


class SubstationTypeUpdateView(generic.UpdateView):
    model = models.SubstationType
    form_class = forms.SubstationTypeForm
    template_name = 'substation_type/update.html'




class SubstationTypeDeleteView(generic.DeleteView):
    model = models.SubstationType
    template_name = 'substation_type/delete.html'
    context_object_name = "city"

    def get_success_url(self):
        return reverse('substation_type:all')
