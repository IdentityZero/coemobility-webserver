from django import forms

from Users.models import AuthUser,UsersProfile
from Vehicles.models import VehiclesVehicles

class UserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ['user_university_number','user_department', 'user_identity', 'user_contact_number' ,'user_image']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user_university_number'].widget.attrs['class'] = 'form-control'
        self.fields['user_department'].widget.attrs['class'] = 'form-control'
        self.fields['user_identity'].widget.attrs['class'] = 'form-control'
        self.fields['user_contact_number'].widget.attrs['class'] = 'form-control'
        self.fields['user_image'].widget.attrs['class'] = 'form-control'

class VehicleForm(forms.ModelForm):
    # Hidden input which will be the reference of the object incase the plate number changes
    vehicle_plate_number0 = forms.CharField(max_length=10, required=False, widget=forms.HiddenInput())
    class Meta:
        model = VehiclesVehicles
        fields = ['vehicle_plate_number', 'vehicle_classification', 'vehicle_model' ,'vehicle_image']

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_plate_number'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_classification'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_model'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_image'].widget.attrs['class'] = 'form-control'

        obj = kwargs.get('instance')

        if obj:
            self.fields['vehicle_plate_number0'].initial = obj.vehicle_plate_number

class NewVehicleForm(forms.ModelForm):
    class Meta:
        model = VehiclesVehicles
        fields = ['vehicle_owner','vehicle_plate_number', 'vehicle_classification', 'vehicle_model','vehicle_image']
        widgets = {
            'vehicle_owner': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(NewVehicleForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_plate_number'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_classification'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_model'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_image'].widget.attrs['class'] = 'form-control'

        self.fields['vehicle_classification'].required = True

        obj = kwargs.get('instance')

        if obj:
            self.fields['vehicle_owner'].initial = obj

       