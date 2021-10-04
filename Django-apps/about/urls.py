from django.urls import path
from about.views import source_code, whoiam


urlpatterns = [
    path('source_code/', source_code),
    path('whoiam/', whoiam),
]
