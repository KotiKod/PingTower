from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = "home"),
    path('my_sites', views.my_sites, name = "my_sites"),
    path('account', views.account, name = "account")
]