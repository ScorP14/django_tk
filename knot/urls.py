from django.urls import path

from django.shortcuts import HttpResponse, render

from knot import views


app_name = 'knot'
urlpatterns = [
    path('', views.KnotListView.as_view(), name='all'),
    path('create/', views.KnotCreateView.as_view(), name='create'),
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('<slug:slug>/update/', views.KnotUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.KnotDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.KnotDetailView.as_view(), name='one'),
]



