from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
   
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(User,CustomUserAdmin)