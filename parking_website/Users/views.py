from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView

from .forms import RegisterForm
from . import models
from Vehicles.models import VehiclesVehicles

# Create your views here.
class UserAccountRegistrationView(FormView):
    template_name = 'Users/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        vehicles = VehiclesVehicles.objects.filter(vehicle_owner=request.user.id).count()
        if self.request.user.is_authenticated and (vehicles == 0):
            return redirect('register-vehicle')
        elif self.request.user.is_authenticated and (vehicles > 0):
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        department = form.cleaned_data['department']
        department_instance = models.UsersDepartment.objects.get(dept_name=department)

        role = form.cleaned_data['role']
        role_instance = models.UsersIdentity.objects.get(identity_name=role)

        contact_number = form.cleaned_data['contact_number']
        university_number = form.cleaned_data['university_number']
        profile_picture = form.cleaned_data['profile_picture']
        print(profile_picture)

        if profile_picture is None:
            profile = models.UsersProfile(user=user,
                                      user_department=department_instance,
                                      user_identity=role_instance,
                                      user_contact_number=contact_number,
                                      user_university_number=university_number)
        else:
            profile = models.UsersProfile(user=user,
                                        user_department=department_instance,
                                        user_identity=role_instance,
                                        user_contact_number=contact_number,
                                        user_university_number=university_number,
                                        user_image=profile_picture)
        profile.save()

        # Login the user
        user = authenticate(username=user.username, password=form.cleaned_data['password'])
        login(self.request,user)

        return redirect('register-vehicle')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

def logout_view(request):
    pass