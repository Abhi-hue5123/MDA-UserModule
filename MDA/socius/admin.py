from django.contrib import admin
from .models import Destination
from .models import UserList , memberdirectory
from import_export.admin import ImportExportModelAdmin
from .models import profile,contactInfo,address,skills,certificate,testimonial,education 
# Register your models here.
admin.site.register(Destination)

admin.site.register(memberdirectory)

admin.site.register(profile)
admin.site.register(contactInfo)
admin.site.register(address)
admin.site.register(skills)
admin.site.register(certificate)
admin.site.register(testimonial)
admin.site.register(education)

admin.site.register(UserList)
class UserListAdmin(ImportExportModelAdmin):
    list_display = ('name','email','coupon','is_superuser')