from django.contrib import admin

from .models import VehiclesVehiclecategory,VehiclesVehicleclassification,VehiclesVehicles,VehiclesVehiclerfid

# Register your models here.
class VehicleCategoryColumn(admin.ModelAdmin):
    list_display = ['vehicle_category']
admin.site.register(VehiclesVehiclecategory,VehicleCategoryColumn)

class VehicleClassificationColumn(admin.ModelAdmin):
    list_display = ['vehicle_classification', 'vehicle_category']
admin.site.register(VehiclesVehicleclassification, VehicleClassificationColumn)

class VehiclesColumn(admin.ModelAdmin):
    list_display = ['vehicle_owner', 'vehicle_plate_number', 'vehicle_classification']
admin.site.register(VehiclesVehicles, VehiclesColumn)

class VehicleRFIDColumn(admin.ModelAdmin):
    list_display = ['vehicle', 'vehicle_rfid']
admin.site.register(VehiclesVehiclerfid, VehicleRFIDColumn)