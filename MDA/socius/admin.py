from django.contrib import admin
from .models import Destination
from .models import UserList
from import_export.admin import ImportExportModelAdmin 
# Register your models here.
admin.site.register(Destination)

admin.site.register(UserList)
class UserListAdmin(ImportExportModelAdmin):
    list_display = ('name','email','coupon')