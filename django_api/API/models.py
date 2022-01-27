# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ShipmentCo2Emissions(models.Model):
    shipment_id = models.IntegerField(blank=True, primary_key=True)
    co2_emission = models.FloatField(blank=True, null=True)
    type_of_calculations = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'shipment_co2_emissions'


class Shipments(models.Model):
    shipment_id = models.CharField(max_length=512, blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)
    pickup_time = models.DateTimeField(blank=True, null=True)
    dropoff_time = models.DateTimeField(blank=True, null=True)

    def co2_default(self):
        try:
            emission = ShipmentCo2Emissions.objects.get(shipment_id=self.id, type_of_calculations="default").co2_emission
        except:
            emission = "-"
        return emission

    def co2_modeled(self):
        try:
            emission = ShipmentCo2Emissions.objects.get(shipment_id=self.id, type_of_calculations="modeled").co2_emission
        except:
            emission = "-"
        return emission

    def co2_primary(self):
        try:
            emission = ShipmentCo2Emissions.objects.get(shipment_id=self.id, type_of_calculations="primary").co2_emission
        except:
            emission = "-"
        return emission

    class Meta:
        db_table = 'shipments'