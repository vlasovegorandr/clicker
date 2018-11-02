from django.conf.urls import url
from . import views

app_name = 'game'

urlpatterns = [
    url(r'^$', views.playscreen, name='playscreen'),
]