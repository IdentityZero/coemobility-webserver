from django import forms
from PIL import Image
import tempfile

from .models import AuthUser,UsersDepartment,UsersIdentity

from .validators import validate_numerics_in_charfields

class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    department = forms.ModelChoiceField(queryset=UsersDepartment.objects.all(), widget=forms.Select(attrs={'class': 'field-input-select'})) # class for designing purposes
    role = forms.ModelChoiceField(queryset=UsersIdentity.objects.all(),  widget=forms.Select(attrs={'class': 'field-input-select'}))
    contact_number = forms.CharField(min_length=11, max_length=20,required=False, validators=[validate_numerics_in_charfields])
    university_number = forms.CharField(max_length=20, required=False,validators=[validate_numerics_in_charfields])
    profile_picture = forms.ImageField(required=False)
    has_agreed = forms.BooleanField(label="I have read and agreed to the terms and conditions.")
    
    class Meta:
        model = AuthUser
        fields = ['username', 'password', 'repeat_password','first_name','last_name','email']

        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def clean_repeat_password(self):
        password = self.cleaned_data['password']
        repeat_password = self.cleaned_data['repeat_password']
        # Add your validation logic here
        if password != repeat_password:
            raise forms.ValidationError("Passwords do not match")
        
        return repeat_password


