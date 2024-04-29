from django.shortcuts import redirect
from django.urls import include, path, re_path

from .views import SubstationViewAll, test, substation_view, main_menu, filter_substation

url_substation = ([
    path('', lambda request: redirect('tk:substation_all_url')),
    path('all/', SubstationViewAll.as_view(), name='substation_all_url'),
    path('create/', test, name='substation_create'),
    path('<str:city>/', filter_substation, name='substation_filter_city_url'),
    path('<str:city>/<str:substation_inside>/', filter_substation, name='substation_filter_city_view_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/', substation_view, name='substation_url'),

    path('<str:city>/<str:substation_inside>/<str:number>/edit/', test, name='substation_edit_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/delete/', test, name='substation_delete_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/photo/', test, name='substation_photo_all_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/photo/1lvl/', test, name='substation_photo_1lvl_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/photo/2lvl/', test, name='substation_photo_2lvl_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/photo/3lvl/', test, name='substation_photo_3lvl_url'),
    path('<str:city>/<str:substation_inside>/<str:number>/photo/<slug:slug_p>/', test, name='substation_the_photo_url'),
])

url_photo = ([
    path('', lambda request: redirect('tk:photo_all_url')),
    path('all/', test, name='photo_all_url'),
    path('create/', test, name='photo_create_url'),



    # Через регулярки
    # re_path(r'^(?P<year>[0-9]{4})/$', test, name='photo_filter_year_url'),
    # re_path(r'^(?P<year>[0-9]{4})/(?P<month>((0[1-9]|[1-9])|1[012]))/$', test, name='photo_filter_year_month_url'),
    # re_path(r'^(?P<year>[0-9]{4})/(?P<month>((0[1-9]|[1-9])|1[012]))/'
    #         r'(?P<day>((0[1-9]|[1-9])|1[012]))/$',test, name='photo_filter_year_month_day_url'),



    path('<int:year>/', test, name='photo_filter_year_url'),
    path('<int:year>/<int:month>/', test, name='photo_filter_year_month_url'),
    path('<int:year>/<int:month>/<int:day>/', test, name='photo_filter_year_month_day_url'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', test, name='photo_url'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/', test, name='photo_edit_url'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete/', test, name='photo_delete_url'),
])

app_name = 'tk'
urlpatterns = [
    path('', main_menu, name='main_menu_url'),
    path('404', test, name='error404_url'),
    path('work_temp/', include(url_substation)),
    path('photo/', include(url_photo)),
]
