from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'main_page/main_menu.html')),
    path('substation/', include('substation.urls')),
    path('knot/', include('knot.urls')),
    path('city/', include('city.urls')),
    path('photo/', include('photo.urls')),
    path('switchgear/', include('switchgear.urls')),
    path('substation-type/', include('substation_type.urls')),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),

    # # path('photo/', include('photo.urls')),
]


# Надо создать шаблон для 404 ошибки
def page_not_found_view(request, exception):
    return render(request, 'basic.html', status=404)


handler404 = page_not_found_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
