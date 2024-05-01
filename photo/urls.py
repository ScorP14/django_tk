from django.urls import path

from django.shortcuts import HttpResponse, render

from photo import views


app_name = 'photo'
urlpatterns = [
    path('', views.PhotoListView.as_view(), name='all'),
    path('create/', views.PhotoCreateView.as_view(), name='create'),
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('<int:pk>/update/', views.PhotoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.PhotoDetailView.as_view(), name='one'),
]



