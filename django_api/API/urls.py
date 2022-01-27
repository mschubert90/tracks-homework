from django.conf.urls import url
from API import views

urlpatterns = [
    url(r"^shipment$", views.shipmentApi)
]