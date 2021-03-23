from django.shortcuts import redirect
from django.urls import include, path

from .views import SubstationViewAll, test, substation_view, main_menu, filter_substation

url_substation = ([
    path('', lambda request: redirect('tk:substation_all_url')),
    path('all/', SubstationViewAll.as_view(), name='substation_all_url'),
    path('create/', test),
    path('<str:city>/', filter_substation),
    path('<str:city>/<str:view>/', filter_substation),
    path('<str:city>/<str:view>/<str:number>/', substation_view, name='substation_url'),

    path('<str:city>/<str:view>/<str:number>/edit/', test),
    path('<str:city>/<str:view>/<str:number>/delete/', test),
    path('<str:city>/<str:view>/<str:number>/photo/', test),
    path('<str:city>/<str:view>/<str:number>/photo/1lvl/', test),
    path('<str:city>/<str:view>/<str:number>/photo/2lvl/', test),
    path('<str:city>/<str:view>/<str:number>/photo/3lvl/', test),
    path('<str:city>/<str:view>/<str:number>/photo/<slug:slug_p>/', test),
])

url_photo = ([
    path('', test),
    path('all/', test),
    path('create/', test),
    path('<int:year>/', test),
    path('<int:year>/<int:month>/', test),
    path('<int:year>/<int:month>/<int:day>/', test),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', test),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/', test),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete/', test),
])

app_name = 'tk'
urlpatterns = [
    path('', main_menu, name='main_menu_url'),
    path('404', test),
    path('substation/', include(url_substation)),
    path('photo/', include(url_photo)),
]


