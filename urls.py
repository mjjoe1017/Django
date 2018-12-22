from foods.views import hello_world
from django.conf.urls import url

urlpatterns = [
    url(r'^hello/$', hello_world),
]
