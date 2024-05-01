from django.urls import reverse
from django.views import generic

from photo import models, forms


class PhotoListView(generic.ListView):
    model = models.Photo
    template_name = "photo/all.html"
    context_object_name = "photos"
    paginate_by = 10


class PhotoDetailView(generic.DetailView):
    model = models.Photo
    template_name = "photo/one.html"
    context_object_name = "photo"


class PhotoUpdateView(generic.UpdateView):
    model = models.Photo
    form_class = forms.PhotoForm
    template_name = 'photo/update.html'


class PhotoCreateView(generic.CreateView):
    model = models.Photo
    form_class = forms.PhotoForm
    template_name = "photo/create.html"
    context_object_name = "photo"


class PhotoDeleteView(generic.DeleteView):
    model = models.Photo
    template_name = 'photo/delete.html'
    context_object_name = "photo"

    def get_success_url(self):
        return reverse('photo:all')
