from django.urls import path, re_path

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.item_list, name='list'),
    re_path('(?P<pk>^[1-9]\\d*)/', views.item_detail)
]
