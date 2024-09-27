from django.urls import path
from .views import  EnquiryCreateView, EnquiryStatusView, FamilyDetailView

urlpatterns = [

    path('enquiry/', EnquiryCreateView.as_view(), name='enquiry_create'),
    path('enquiry/<int:pk>/status/', EnquiryStatusView.as_view(), name='enquiry_status'),
    path('family/', FamilyDetailView.as_view(), name='family-details'),
   
]
