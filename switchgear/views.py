from django.urls import reverse
from django.views import generic

from switchgear import models, forms


class SwitchgearListView(generic.ListView):
    model = models.Switchgear
    template_name = "switchgear/all.html"
    context_object_name = "switchgears"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('title')


class SwitchgearDetailView(generic.DetailView):
    model = models.Switchgear
    template_name = "switchgear/one.html"
    context_object_name = "switchgear"



class SwitchgearCreateView(generic.CreateView):
    model = models.Switchgear
    form_class = forms.SwitchgearForm
    template_name = "switchgear/create.html"
    context_object_name = "switchgear"


class SwitchgearUpdateView(generic.UpdateView):
    model = models.Switchgear
    form_class = forms.SwitchgearForm
    template_name = 'switchgear/update.html'




class SwitchgearDeleteView(generic.DeleteView):
    model = models.Switchgear
    template_name = 'switchgear/delete.html'
    context_object_name = "switchgear"

    def get_success_url(self):
        return reverse('switchgear:all')
