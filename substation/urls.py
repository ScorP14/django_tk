
from django.urls import path

from django.shortcuts import HttpResponse, render, redirect

from . import views
from .forms import SubstationForm



urlpatterns_city = (
[
    path('', lambda r: HttpResponse('Все сити'), name='city_all'),
    path('<str:pk>/', lambda r, pk: HttpResponse(f'Один Сити'), name='city_one'),
],
    'city_url'
)



app_name = 'substation'
urlpatterns = [
    path('search/', lambda r: HttpResponse('search'), name='search_url'),
    path('create/', views.SubstationCreateView.as_view(), name='create_url'),
    #
    path('', views.SubstationsListView.as_view(), name='all_url'),

    # -------------------------------
    # -------URL Substation----------
    # -------------------------------
    path('<int:pk>/', lambda r, pk: redirect('substation:get_one_url'), name='get_one_from_pk_url'),
    path('<slug:slug>/photo/', lambda _, slug: HttpResponse('photo'), name='photo'),
    path('<slug:slug>/update/', views.SubstationUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.SubstationDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.SubstationDetailView.as_view(), name='get_one_url'),
    # -------------------------------
]




'''
http://127.0.0.1:8000/photo/search/<int:year>/<int:month>/<int:day>/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/substation/     --->    /work_temp/ysole-gpp-1/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/update/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/delete/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/
http://127.0.0.1:8000/photo/
'''
