
from django.urls import path

from django.shortcuts import HttpResponse, render, redirect

from . import views
from .forms import SubstationForm

app_name = 'substation'
urlpatterns = [
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('create/', views.SubstationCreateView.as_view(), name='create'),
    #
    path('', views.SubstationsListView.as_view(), name='all'),

    # -------------------------------
    # -------URL Substation----------
    # -------------------------------
    path('<int:pk>/', lambda r, pk: redirect('substation:get_one_'), name='get_one_from_pk'),
    path('<slug:slug>/photo/', lambda _, slug: HttpResponse('photo'), name='photo'),
    path('<slug:slug>/update/', views.SubstationUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.SubstationDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.SubstationDetailView.as_view(), name='get_one'),
    # -------------------------------
]




