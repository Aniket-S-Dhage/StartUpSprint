from django.urls import path, include
from .views import ApplicationCreateView, ApplicationStatusView,BankDetailsView, UserDetailView


urlpatterns = [
    path('applications/', ApplicationCreateView.as_view()),
    path('applications/status/<int:id>/', ApplicationStatusView.as_view()),
    path('bank-details/', BankDetailsView.as_view(), name='bank-details'),
    path('bank-details/<ifsc_code>/', BankDetailsView.as_view(), name='bank-details-ifsc'),
    path('user_details/', UserDetailView.as_view(), name='user-details'),


   
]
