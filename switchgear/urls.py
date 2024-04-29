from django.urls import path

from django.shortcuts import HttpResponse, render

from switchgear import views


app_name = 'switchgear'
urlpatterns = [
    path('', views.SwitchgearListView.as_view(), name='all'),
    path('create/', views.SwitchgearCreateView.as_view(), name='create'),
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('<slug:slug>/update/', views.SwitchgearUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.SwitchgearDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.SwitchgearDetailView.as_view(), name='one'),
]



