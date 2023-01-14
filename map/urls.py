from django.urls import path
from .views import (
    MapView,
    CountryView,
)
from . import views

urlpatterns = [
    path('', MapView.as_view(), name="map-home"),
    path('country/<int:pk>', CountryView.as_view(), name="country"),

]
