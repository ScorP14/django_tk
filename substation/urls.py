
from django.urls import path

from django.shortcuts import HttpResponse, render, redirect

from . import views
from .forms import SubstationForm


app_name = 'substation'
urlpatterns = [
    path('search/', lambda r: HttpResponse('search'), name='search_url'),
    path('create/', lambda r: HttpResponse('create'), name='create_url'),
    #
    path('', views.SubstationsListView.as_view(), name='all_url'),

    # path('city/', include(city_urls)),

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
