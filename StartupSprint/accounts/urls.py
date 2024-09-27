from django.urls import path
from .views import register_user
from .views import CustomerListView


urlpatterns = [
    path('register/', register_user, name='create_user'),
    path('api/customers/', CustomerListView.as_view(), name='customer-list')
]
