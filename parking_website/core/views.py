from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView

from Users.models import UsersIdentity,UsersProfile
from Vehicles.models import VehiclesVehiclecategory,VehiclesVehicles
from .forms import UserForm, ProfileForm, VehicleForm,NewVehicleForm

def home(request):
    if not request.user.is_authenticated:
            return redirect('login')

    user = request.user
    # Get vehicle category aswell !TODO
    user_role = user.usersprofile.user_identity
    vehicle_categories = VehiclesVehiclecategory.objects.all()
    roles = UsersIdentity.objects.all()
    roles = roles.exclude(pk=user_role.id)

    context = {'priority_role': user_role,
               'vehicle_categories':vehicle_categories,
               'roles':roles,
               'THUMBNAIL_BUCKET_URL' : settings.THUMBNAIL_BUCKET_URL,
               'DATA_SERVER_URL':settings.DATA_SERVER_URL}
    
    return render(request, 'core/home.html', context)

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'core/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['THUMBNAIL_BUCKET_URL'] = settings.THUMBNAIL_BUCKET_URL
        user = self.request.user
        vehicles = VehiclesVehicles.objects.filter(vehicle_owner=user)

        vehicle_data_form_coupling = []

        for vehicle in vehicles:
            vehicle_instance = vehicle
            form = VehicleForm(instance=vehicle_instance)
            dict = {
                "instance": vehicle_instance,
                "form": form 
            }

            vehicle_data_form_coupling.append(dict)

        context['vehicles'] = vehicle_data_form_coupling
        context['UserForm'] = UserForm(instance=user)
        users_profile = UsersProfile.objects.get(user=user)
        context['ProfileForm'] = ProfileForm(instance=users_profile)

        context['NewVehicleForm'] = NewVehicleForm(instance=user)
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def post(self,request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Checkers are used to differentiate the forms
        # For editing profile and user
        user = self.request.user
        user_profile = UsersProfile.objects.get(user=user)

        try:
            userFormChecker = request.POST['username']
            userProfileFormChecker = request.POST['user_university_number']
            userForm = UserForm(request.POST, instance=user)
            userProfileForm = ProfileForm(request.POST,request.FILES, instance=user_profile)
            print("Saving profile")
            if userForm.is_valid() and userProfileForm.is_valid():
                print("Saving profile: success...")
                userForm.save()
                userProfileForm.save()
            elif not userForm.is_valid():
                print("Invalid userform")
                error_message = userForm.errors
                context['error_list'] = error_message
                return self.render_to_response(context)
            elif not userProfileForm.is_valid():
                print("Invalid profile form")
                error_message = userProfileForm.errors
                context['error_list'] = error_message
                return self.render_to_response(context)

        except:
            print("Error")

        # For editing vehicle
        try:
            vehicle_instance = VehiclesVehicles.objects.get(vehicle_plate_number=request.POST['vehicle_plate_number0'])
            vehicleForm = VehicleForm(request.POST,request.FILES, instance=vehicle_instance)
            if vehicleForm.is_valid():
                vehicleForm.save()
            else:
                error_message = vehicleForm.errors
                context['error_list'] = error_message
                return self.render_to_response(context)
        except:
            pass

        # For adding new vehicle
        try:
            checker = request.POST['vehicle_owner']
            newVehicleForm = NewVehicleForm(request.POST)
            if newVehicleForm.is_valid():
                newVehicleForm.save()

            else:
                error_message = newVehicleForm.errors
                context['error_list'] = error_message
                return self.render_to_response(context)
        except:
            pass
        
        return redirect('profile')

def records(request):
    context = {
        'THUMBNAIL_BUCKET_URL' : settings.THUMBNAIL_BUCKET_URL
    }
    return render(request,'core/records.html', context)
