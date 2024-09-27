from django.contrib import admin

from django.contrib import admin
from .models import Application, Guarantor


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'aadhaar_no', 'pan_no', 'type_of_employment', 'business_type', 'status', 'application_timestamp')  
    search_fields = ('user__username', 'aadhaar_no', 'pan_no', 'status')  
    list_filter = ('type_of_employment', 'business_type', 'status') 


class GuarantorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'relation_with_customer', 'gender', 'email', 'mobile', 'city', 'state', 'country') 
    search_fields = ('name', 'relation_with_customer', 'email', 'mobile')  
    list_filter = ('gender', 'city', 'state', 'country')  


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Guarantor, GuarantorAdmin)

