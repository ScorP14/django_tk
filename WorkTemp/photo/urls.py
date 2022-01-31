from django.contrib.auth import views
from django.urls import path, include
from . import views

urlpatterns = [
        path('login/', lambda re:print(re), name='login'),
]
