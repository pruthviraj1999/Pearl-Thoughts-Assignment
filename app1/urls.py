# appointments/urls.py

from django.urls import path
from . import views
from .views import DoctorList, DoctorDetail, AppointmentCreate

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('appointments/', AppointmentCreate.as_view(), name='appointment-create'),
]
