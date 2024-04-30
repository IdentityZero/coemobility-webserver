from django.contrib import admin
from .models import UsersDepartment, AuthUser,UsersProfile, UsersIdentity

# Register your models here.
class UsersDepartmentColumn(admin.ModelAdmin):
    list_display = ['dept_abbr', 'dept_name']
admin.site.register(UsersDepartment, UsersDepartmentColumn)


class UsersIdentityColumn(admin.ModelAdmin):
    list_display = ['identity_name']
admin.site.register(UsersIdentity, UsersIdentityColumn)


class UsersIdentityColumn(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
admin.site.register(AuthUser,UsersIdentityColumn )


class UsersIdentityColumn(admin.ModelAdmin):
    list_display = ['user', 'user_department', 'user_identity', 'user_university_number', 'user_contact_number']
admin.site.register(UsersProfile,UsersIdentityColumn)


admin.site.site_header = 'Coemobility Administration'