from django.contrib import admin
from .models import UsersDepartment, AuthUser,UsersProfile, UsersIdentity

# Register your models here.
admin.site.register(UsersDepartment)
admin.site.register(UsersIdentity)
admin.site.register(AuthUser)
admin.site.register(UsersProfile)

admin.site.site_header = 'Coemobility Administration'