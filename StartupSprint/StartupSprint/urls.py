from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh


urlpatterns = [
    path('admin/', admin.site.urls),
    path('e1/', include('customer.urls')),
    path('app/', include('application_generation.urls')),
    path('api/token/', token_obtain_pair, name='token_obtain_pair'),  
    path('api/auth/refresh/', token_refresh, name='token_refresh'),  
        
]
