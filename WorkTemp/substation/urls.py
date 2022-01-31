from django.contrib.auth import views
from django.urls import path, include
from . import views
from django.http import HttpResponse



urlpatterns = [
        path('', views.main_menu, name='main_menu'),
]


'''

url_substation = ([
    path('', lambda request: redirect('tk:substation_all_url')),
    path('all/', SubstationViewAll.as_view(), name='substation_all_url'),
    path('create/', test, name='substation_create'),
    path('<str:city>/', filter_substation, name='substation_filter_city_url'),
    path('<str:city>/<str:view>/', filter_substation, name='substation_filter_city_view_url'),
    path('<str:city>/<str:view>/<str:number>/', substation_view, name='substation_url'),
    path('<str:city>/<str:view>/<str:number>/edit/', test, name='substation_edit_url'),
    path('<str:city>/<str:view>/<str:number>/delete/', test, name='substation_delete_url'),
    path('<str:city>/<str:view>/<str:number>/photo/', test, name='substation_photo_all_url'),
    path('<str:city>/<str:view>/<str:number>/photo/1lvl/', test, name='substation_photo_1lvl_url'),
    path('<str:city>/<str:view>/<str:number>/photo/2lvl/', test, name='substation_photo_2lvl_url'), 
    path('<str:city>/<str:view>/<str:number>/photo/3lvl/', test, name='substation_photo_3lvl_url'),

    ])'''
