from django.urls import reverse
from django.views import generic

from knot import models, forms


class KnotListView(generic.ListView):
    model = models.Knot
    template_name = "knot/all.html"
    context_object_name = "knots"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('title')


class KnotDetailView(generic.DetailView):
    model = models.Knot
    template_name = "knot/one.html"
    context_object_name = "knot"


class KnotCreateView(generic.CreateView):
    model = models.Knot
    form_class = forms.KnotForm
    template_name = "knot/create.html"
    context_object_name = "knot"


class KnotUpdateView(generic.UpdateView):
    model = models.Knot
    form_class = forms.KnotForm
    template_name = 'knot/update.html'


class KnotDeleteView(generic.DeleteView):
    model = models.Knot
    template_name = 'knot/delete.html'
    context_object_name = "knot"

    def get_success_url(self):
        return reverse('knot:all')
