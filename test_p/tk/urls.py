from django.shortcuts import redirect
from django.urls import include, path

from django.http import HttpResponse

from .views import *

app_name = 'tk'
urlpatterns = [
    path('', main_menu, name='main_menu_url'),
    path('404', test),

    path('substation', lambda request: redirect('tk:substation_all_url')),
    path('substation/all', SubstationViewAll.as_view(), name='substation_all_url'),
    path('substation/create', test),

    path('substation/<str:city>', test),
    path('substation/<str:city>/<str:tp>', SubstationView, name='substation_url'),
    path('substation/<str:city>/<slug:slug>/edit', test),
    path('substation/<str:city>/<slug:slug>/delete', test),

    path('substation/<str:city>/<slug:slug>/photo', test),
    path('substation/<str:city>/<slug:slug>/photo/1lvl', test),
    path('substation/<str:city>/<slug:slug>/photo/2lvl', test),
    path('substation/<str:city>/<slug:slug>/photo/3lvl', test),
    path('substation/<str:city>/<slug:slug>/photo/<slug:slug_p>', test),

  #  path('substation/<slug:slug>', SubstationView.as_view(), name='substation_url'),

    path('photo', test),
    path('photo/all', test),
    path('photo/create', test),

    path('photo/<int:year>', test),
    path('photo/<int:year>/<int:month>', test),
    path('photo/<int:year>/<int:month>/<int:day>', test),
    path('photo/<int:year>/<int:month>/<int:day>/<slug:slug>', test),
    path('photo/<int:year>/<int:month>/<int:day>/<slug:slug>/edit', test),
    path('photo/<int:year>/<int:month>/<int:day>/<slug:slug>/delete', test),
]
