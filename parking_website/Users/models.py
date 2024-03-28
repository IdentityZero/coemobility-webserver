from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .validators import validate_password_strength,validate_numerics_in_charfields

# Create your models here.

class AuthUser(AbstractUser):
    password = models.CharField(max_length=128, validators=[validate_password_strength])
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'auth_user'


class UsersDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    dept_abbr = models.CharField(unique=True, max_length=10)
    dept_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users_department'
    
    def __str__(self):
        return self.dept_name


class UsersIdentity(models.Model):
    id = models.BigAutoField(primary_key=True)
    identity_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'users_identity'
    
    def __str__(self):
        return self.identity_name


class UsersProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    user_department = models.ForeignKey(UsersDepartment, models.DO_NOTHING, blank=True, null=True)
    user_identity = models.ForeignKey(UsersIdentity, models.DO_NOTHING, blank=True, null=True)
    user_image = models.ImageField(upload_to="profile_pics", default="profile_pics/profile.png")
    user_contact_number = models.CharField(max_length=20, blank=True, null=True, validators=[validate_numerics_in_charfields])
    user_university_number = models.CharField(max_length=20, blank=True, null=True, validators=[validate_numerics_in_charfields])

    class Meta:
        managed = False
        db_table = 'users_profile'

