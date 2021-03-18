from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


from .models import *



def main_menu(request):
    photos = Photo.objects.all()
    return render(request, 'tk/main_menu.html', {'photos': photos})



class SubstationAll(View):
    model = Substation
    template = 'tk/substation_all.html'

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, {self.model.lower(): obj})
