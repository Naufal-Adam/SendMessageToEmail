from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.send_test, name='send_bro'),
]