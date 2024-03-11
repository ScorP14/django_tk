# from django.contrib.auth import views
from django.urls import path  # , include
# from django.http import HttpResponse
from django.shortcuts import redirect, HttpResponse

from . import views

app_name = 'substation'

urlpatterns = [
    path('', lambda _: redirect('substation:all_url')),
    path('all/', views.SubstationsView.as_view(), name='all_url'),
    path('<int:tp>/', views.get_substation_for_id, name='get_url'),
    # path('create/', lambda r: HttpResponse('create'), name='create'),
    # path('<str:city>/', views.search_by_args, name='search_url'),
    # path('<str:city>/<str:view>/', views.search_by_args, name='search_url'),
    # path('<str:city>/<str:view>/<str:number>/', views.search_by_args, name='search_url'),

    # path('<str:city>/<str:view>/<str:number>/edit/', lambda *a,**kwargs:HttpResponse(f'тп едит {kwargs})'), name='edit_url'),
    # path('<str:city>/<str:view>/<str:number>/delete/', lambda *a,**kwargs:HttpResponse(f'тп делете {kwargs})'), name='delete_url'),
    # path('<str:city>/<str:view>/<str:number>/photo/', lambda *a,**k:HttpResponse(f'фотки подсьанций{k})'), name='photo_all_url'),
    # path('<str:city>/<str:view>/<str:number>/photo/lvl1', lambda *a,**kwargs:HttpResponse(f'нач. деф{kwargs})'), name='photo_lvl1_url'),
    # path('<str:city>/<str:view>/<str:number>/photo/lvl2', lambda *a,**kwargs:HttpResponse(f'ср. деф.{kwargs})'), name='photo_lvl2_url'),
    # path('<str:city>/<str:view>/<str:number>/photo/lvl3', lambda *a,**kwargs:HttpResponse(f'авар. деф{kwargs})'), name='photo_lvl3_url'),

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
