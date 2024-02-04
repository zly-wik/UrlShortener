from django.urls import path

from core.views import index


urlpatterns = [
    path('', index),
    path('<slug:code>/', index),
]
