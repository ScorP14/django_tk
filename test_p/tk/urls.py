from django.urls import include, path


from django.http import HttpResponse

from .views import *



app_name = 'tk'
urlpatterns = [
        path('', main_menu, name='main_menu'),

        #path('/404/', tp),        




        #path('/tp/all/', tp),
        #path('/tp/create/', tp),
        #path('/tp/<slug:slug>/', tp),
        #path('/tp/<slug:slug>/edit/', tp),
        #path('/tp/<slug:slug>/delete/', tp),

        #path('/tp/<slug:slug>/photo/', tp),
        #path('/tp/<slug:slug>/photo/<slug:slug>', tp),
        #path('/tp/<slug:slug>/photo/1lvl', tp),
        #path('/tp/<slug:slug>/photo/2lvl', tp),
        #path('/tp/<slug:slug>/photo/3lvl', tp),
        

        #path('/photo/all/', tp),    
        #path('/photo/all/<year:int>/', tp),
        #path('/photo/all/<year:int>/<month:int>/', tp),
        #path('/photo/all/<year:int>/<month:int>/<day:int>/', tp),


        #path('/photo/create/', tp),
        #path('/photo/<slug:slug>/', tp),
        #path('/photo/<slug:slug>/edit/', tp),
        #path('/photo/<slug:slug>/delete/', tp),
    ]





