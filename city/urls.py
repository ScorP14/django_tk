from django.urls import path

from django.shortcuts import HttpResponse, render

from city import views


def test(request):
    context = {
        'obj': [f'Город - {i}' for i in range(50)]
    }
    return render(request, 'test.html', context)


app_name = 'city'
urlpatterns = [
    path('test/', lambda r: test(r), name='1'),

    path('', views.CityListView.as_view(), name='all'),
    path('create/', lambda r: HttpResponse('Создать сити create'), name='create'),
    path('<str:pk>/', lambda r, pk: HttpResponse(f'Один {pk=}'), name='one'),
    path('search/', lambda r: HttpResponse('search'), name='search'),
    path('<slug:slug>/update/', views.CityUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.CityDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', views.CityDetailView.as_view(), name='get_one'),
]



