
from django.urls import path

from django.shortcuts import HttpResponse, render, redirect

from . import views


app_name = 'substation'

urlpatterns = [
    # path('search/', test_qwe, name='search'), # lambda r: HttpResponse('search')
    path('create/', views.SubstationCreateView.as_view(), name='create'),
    #
    path('', views.SubstationsListView.as_view(), name='all'),

    # -------------------------------
    # -------URL Substation----------
    # -------------------------------
    path('<int:pk>/', lambda r, pk: redirect('substation:one'), name='get_one_from_pk'),
    path('<slug:slug>/photo/', lambda _, slug: HttpResponse('photo'), name='photo'),
    path('<slug:slug>/update/', views.SubstationUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.SubstationDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.SubstationDetailView.as_view(), name='one'),
    # -------------------------------
]




