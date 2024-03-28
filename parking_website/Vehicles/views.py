from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

import re

from Users.models import AuthUser
from .models import VehiclesVehiclecategory,VehiclesVehicleclassification, VehiclesVehicles,VehiclesVehiclerfid
from .forms import VehicleRegistrationForm

def vehicleTrialView(request):
    string_with_numbers = "abc543123def456ghi"

    # Remove non-numeric characters
    result = re.sub(r'\D', '', string_with_numbers)

    print(result)  # Output: 123456
        # Your logic here
    return HttpResponse("Hello, world!")

class VehicleRegistrationFormView(FormView):
    # !TODO If the form contains the same plate number
    # !TODO Error handling for additional entries handled in js
    template_name = "Vehicles/register-vehicle.html"
    form_class = VehicleRegistrationForm

    def dispatch(self, request, *args, **kwargs):
        vehicles = VehiclesVehicles.objects.filter(vehicle_owner=request.user.id).count()

        if self.request.user.is_authenticated and (vehicles > 0):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):

        owner = self.request.user

        # Unpack first vehicle instance details
        vehicle_classification = form.cleaned_data['vehicle_classification']
        vehicle_plate_number = form.cleaned_data['vehicle_plate_number']
        vehicle_image = form.cleaned_data['vehicle_image']
        vehicle_model = form.cleaned_data['vehicle_model']

        initial_vehicle = VehiclesVehicles(vehicle_plate_number=vehicle_plate_number,
                                           vehicle_classification=vehicle_classification,
                                           vehicle_owner =owner,
                                           vehicle_image=vehicle_image,
                                           vehicle_model=vehicle_model)
        initial_vehicle.save()

        # For additional vehicles
        vehicle_detail_dict = {}

        # Unpack additional vehicle instance details
        keys = list(form.data.keys()) # Get all the input names from the form
        print(keys)
        # Remove the keys of the first instance, and the csrf token
        keys_to_remove = ['csrfmiddlewaretoken', 'vehicle_model', 'vehicle_classification', 'vehicle_plate_number', 'vehicle_image']
        keys = list(filter(lambda x: x not in keys_to_remove, keys))
        print(keys)

        # Get other instances. The other instances are determined and packed based on the last number of the keys
        key_ids = list(set([re.sub(r'\D', '', s) for s in keys]))

        if not key_ids:
            return redirect('home')

        # Package related instances
        for key_id in key_ids:
            vehicle_detail_dict[key_id] = {}
            for key in keys:
                key_id_of_i_key = re.sub(r'\D', '', key)
                key_name_of_i_key = re.sub(r'\d', '', key)

                if key_id == key_id_of_i_key:
                    vehicle_detail_dict[key_id][key_name_of_i_key] = form.data[key]
        
        for key,value in vehicle_detail_dict.items():
            plate_number = value['vehicle_plate_number']

            model = value['vehicle_model']
            classification = value['vehicle_classification']
            classification = VehiclesVehicleclassification.objects.get(id=classification)

            # Files not from the original form is sent through self.request.FILES
            try:
                image = value['vehicle_image']
            except KeyError:
                image = self.request.FILES[f"vehicle_image{key}"]

            if image == "":
                    additional_car = VehiclesVehicles(vehicle_plate_number=plate_number,
                                            vehicle_classification=classification,
                                            vehicle_owner =owner,
                                            vehicle_model=model)
            else:
                additional_car = VehiclesVehicles(vehicle_plate_number=plate_number,
                                            vehicle_classification=classification,
                                            vehicle_owner =owner,
                                            vehicle_image=image,
                                            vehicle_model=model)
            
            additional_car.save()

        return redirect('home')

