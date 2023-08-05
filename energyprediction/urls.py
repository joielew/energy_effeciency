from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_energy_consumption, name='predict_energy_consumption')
]
