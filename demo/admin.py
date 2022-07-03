from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from demo.models import CustomerUser, InOut
# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomerUser,UserModel)

admin.site.register(InOut)