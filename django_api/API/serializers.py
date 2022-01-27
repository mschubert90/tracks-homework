from rest_framework import serializers
from API.models import *

class ShipmentsSerializer(serializers.ModelSerializer):

    co2_default = serializers.CharField()
    co2_modeled = serializers.CharField()
    co2_primary = serializers.CharField()

    class Meta:
        model=Shipments
        fields=('shipment_id', 'weight_kg', 'distance_km', 'pickup_time', 'dropoff_time', 'co2_default', 'co2_modeled', 'co2_primary')