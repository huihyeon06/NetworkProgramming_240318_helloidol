from django.urls import path

from txtview import views

app_name='txt'

urlpatterns=[
    path('subin/', views.show_subin, name='subin'),
    path('yeonjun/', views.show_yeonjun, name='yeonjun'),
    path('teahyeon/', views.show_teahyeon, name='teahyeon'),
    path('huning/', views.show_huning, name='huning'),
    path('bumgue/', views.show_bumgue, name='bumgue'),
]