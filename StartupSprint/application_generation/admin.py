from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'aadhaar_no', 'pan_no', 'type_of_employment', 'status'] 
    search_fields = ['aadhaar_no', 'pan_no', 'user__username'] 

admin.site.register(Application, ApplicationAdmin)

