from django.contrib import admin

from django.contrib import admin
from .models import Family, Bank


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('user', 'father_name', 'mother_name', 'marital_status', 'spouse_name')  
    search_fields = ('father_name', 'mother_name', 'spouse_name') 
    list_filter = ('marital_status',)  


class BankAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank_name', 'account_number', 'ifsc_code')  
    search_fields = ('bank_name', 'account_number')  
    list_filter = ('bank_name',)  


admin.site.register(Family, FamilyAdmin)
admin.site.register(Bank, BankAdmin)

