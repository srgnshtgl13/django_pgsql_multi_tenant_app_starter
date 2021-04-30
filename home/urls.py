from django.urls import path

from . import views

app_name = 'home'    # now we can use the urls in the template syntax like that {% account:login %}

urlpatterns = [
    path('', views.index, name='home'),
]