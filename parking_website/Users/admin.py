from django.contrib import admin
from .models import UsersDepartment, AuthUser,UsersProfile

# Register your models here.
admin.site.register(AuthUser)
admin.site.register(UsersProfile)
admin.site.register(UsersDepartment)