from django.db import models
from Users.models import AuthUser

# Create your models here.
class VehiclesVehiclecategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_category = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Vehicles_vehiclecategory'
        verbose_name = "Vehicle Category"
        verbose_name_plural = "Vehicle Categories"
    
    def __str__(self):
        return self.vehicle_category
    
class VehiclesVehicleclassification(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_classification = models.CharField(max_length=30)
    vehicle_category = models.ForeignKey(VehiclesVehiclecategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vehicles_vehicleclassification'
        verbose_name = "Vehicle Classification"
        verbose_name_plural = "Vehicle Classifications"
    
    def __str__(self):
        return self.vehicle_classification

class VehiclesVehicles(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_plate_number = models.CharField(unique=True, max_length=10)
    vehicle_classification = models.ForeignKey(VehiclesVehicleclassification, models.DO_NOTHING, blank=True, null=True)
    vehicle_owner = models.ForeignKey(AuthUser, models.DO_NOTHING)
    vehicle_image = models.ImageField(upload_to="vehicle_pics", default="vehicle_pics/vehicle.png")
    vehicle_model = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vehicles_vehicles'
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

class VehiclesVehiclerfid(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_rfid = models.CharField(unique=True, max_length=32)
    vehicle = models.ForeignKey('VehiclesVehicles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Vehicles_vehiclerfid'
        verbose_name = "Vehicle RFID"
        verbose_name_plural = "Vehicle RFIDs"

