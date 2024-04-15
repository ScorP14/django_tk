from django.urls import path

from django.shortcuts import HttpResponse, render, redirect

from city import views

app_name = 'city'

urlpatterns = [
    path('', views.CityListView.as_view(), name='all_url'),
    path('create/', lambda r: HttpResponse('Создать сити'), name='create_url'),
    path('<str:pk>/', lambda r, pk: HttpResponse(f'Один {pk}'), name='city_one'),
    # path('search/', lambda r: HttpResponse('search'), name='search_url'),

    path('<slug:slug>/update/', views.CityUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.CityDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.CityDetailView.as_view(), name='get_one_url'),
]



