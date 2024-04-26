from django.urls import path

from django.shortcuts import HttpResponse, render

from city import views


app_name = 'city'
urlpatterns = [
    # path('test/', lambda r: test(r), name='1'),

    path('', views.CityListView.as_view(), name='all'),
    path('create/', views.CityCreateView.as_view(), name='create'),
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('<slug:slug>/update/', views.CityUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.CityDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.CityDetailView.as_view(), name='one'),
]



