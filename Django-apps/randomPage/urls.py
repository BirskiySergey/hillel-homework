from django.urls import path
from randomPage.views import index


urlpatterns = [
    path('', index),
]
