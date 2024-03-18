
from django.urls import path

from django.shortcuts import HttpResponse, render, redirect


app_name = 'city'

urlpatterns = [
    path('', lambda r: HttpResponse('Все сити'), name='all_url'),
    path('create/', lambda r: HttpResponse('Создать сити'), name='create_url'),
    path('<str:pk>/', lambda r, pk: HttpResponse(f'Один Сити'), name='city_one'),
    # path('search/', lambda r: HttpResponse('search'), name='search_url'),



    # path('<int:pk>/', lambda r, pk: redirect('substation:get_one_url'), name='get_one_from_pk_url'),
    # path('<slug:slug>/photo/', lambda _, slug: HttpResponse('photo'), name='photo'),
    # path('<slug:slug>/update/', views.SubstationUpdateView.as_view(), name='update'),
    # path('<slug:slug>/delete/', views.SubstationDeleteView.as_view(), name='delete'),
    # path('<slug:slug>/', views.SubstationDetailView.as_view(), name='get_one_url'),
    # -------------------------------
]



