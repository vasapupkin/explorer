from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^home$', views.index, name='home'),
    re_path(r'^account$', views.account, name='account'),
    path('post/ajax/search/wallet', views.search, name = "search_wallet")
]
