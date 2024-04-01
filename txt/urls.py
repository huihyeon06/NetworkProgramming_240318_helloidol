from django.urls import path

from txt import views

app_name='txt'

urlpatterns=[
    path('<멤버>/', views.show_멤버, name='멤버'),
    # path('subin/', views.show_, name='subin'),
    # path('yeonjun/', views.show_yeonjun, name='yeonjun'),
    # path('teahyeon/', views.show_teahyeon, name='teahyeon'),
    # path('huning/', views.show_huning, name='huning'),
    # path('bumgue/', views.show_bumgue, name='bumgue'),
]