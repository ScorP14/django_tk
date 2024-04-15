from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .forms import SubstationForm
from .models import Substation, RepositorySubstation


class SubstationCreateView(generic.CreateView):
    model = Substation
    form_class = SubstationForm
    template_name = 'substation/create.html'

    def post(self,  req):
        form = SubstationForm(req.POST)

        # print(req.POST['city'])
        tp = RepositorySubstation.get_or_none(city=req.POST['city'], view=req.POST['view'], number=req.POST['number'])
        # print(tp)
        # if form.is_valid():
        #     if RepositorySubstation.get()
        return HttpResponse('Possst')

   # form = ReviewForm(request.POST)
   #      movie = Movie.objects.get(id=pk)
   #      if form.is_valid():
   #          form = form.save(commit=False)
   #          if request.POST.get("parent", None):
   #              form.parent_id = int(request.POST.get("parent"))
   #          form.movie = movie
   #          form.save()
   #      return redirect(movie.get_absolute_url())

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
        return reverse('substation:all_url')


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
