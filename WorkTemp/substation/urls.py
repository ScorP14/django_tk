from django.urls import path

from django.shortcuts import HttpResponse

from . import views


def test_func(request):
    return HttpResponse('')


app_name = 'substation'

urlpatterns = [
    path('123/', test_func),

    path('search/', lambda r: HttpResponse('search'), name='search_url'),
    path('create/', lambda r: HttpResponse('create'), name='create_url'),

    path('<slug:slug>/photo/', lambda r: HttpResponse('photo')),
    path('<slug:slug>/update/', lambda r: HttpResponse('update')),
    path('<slug:slug>/delete/', lambda r: HttpResponse('delete')),
    path('<slug:slug>/', views.SubstationDetailView.as_view(), name='get_one_url'),

    path('<int:pk>/', lambda r: HttpResponse('pk редирект в slug'), name='get_one_from_pk_url'),

    path('', views.SubstationsListView.as_view(), name='all_url'),

]

'''
http://127.0.0.1:8000/photo/search/<int:year>/<int:month>/<int:day>/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/substation/     --->    /substation/ysole-gpp-1/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/update/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/delete/
http://127.0.0.1:8000/photo/2024-02-20-iv-01555/
http://127.0.0.1:8000/photo/
'''
