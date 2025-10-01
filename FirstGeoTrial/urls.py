from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.location_page, name='location_page'),
    path('report/', views.report_location, name='report_location'),
]
