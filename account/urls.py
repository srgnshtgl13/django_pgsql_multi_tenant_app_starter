from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'    # now we can use the urls in the template syntax like that {% account:login %}
urlpatterns = [
    # use custom login system
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('logout/', views.logout_view, name='logout')

    # use built in login system
    # path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
]