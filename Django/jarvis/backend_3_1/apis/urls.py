from django.urls import path
from .views import weather

urlpatterns = [
    # path('', weather.helloworld)
    # path('', weather.weather)
    path('weather', weather.weather)
]
