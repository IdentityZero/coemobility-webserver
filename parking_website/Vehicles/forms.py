from django import forms

from .models import VehiclesVehiclecategory,VehiclesVehicleclassification, VehiclesVehicles,VehiclesVehiclerfid

class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model = VehiclesVehicles
        fields = ['vehicle_plate_number', 'vehicle_classification', 'vehicle_model','vehicle_image']

        widgets = {
            'vehicle_classification': forms.Select(attrs={'class': 'field-input-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(VehicleRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_classification'].required = True