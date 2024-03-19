
from django.views import generic

from city.models import City


# Create your views here.
class CityListView(generic.ListView):
    model = City
    template_name = "city/all.html"
    context_object_name = "citys"
    paginate_by = 10



class CityDetailView(generic.DetailView):
    model = City
    template_name = "city/one.html"
    context_object_name = "city"
