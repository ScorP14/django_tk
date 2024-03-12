"""WorkTemp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', lambda request: render(request, 'main_page/main_menu.html')),
    path('substation/', include('substation.urls')),
    # path('photo/', include('photo.urls')),
    path('admin/', admin.site.urls)
]


# Надо создать шаблон для 404 ошибки
def page_not_found_view(request, exception):
    return render(request, 'basic.html', status=404)


handler404 = page_not_found_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
