from django.urls import path
from django.shortcuts import HttpResponse

from substation_type import views


app_name = 'substation_type'
urlpatterns = [
    path('', views.SubstationTypeListView.as_view(), name='all'),
    path('create/', views.SubstationTypeCreateView.as_view(), name='create'),
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('<slug:slug>/update/', views.SubstationTypeUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.SubstationTypeDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.SubstationTypeDetailView.as_view(), name='one'),
]



