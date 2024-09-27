from rest_framework import serializers
from .models import Application, Guarantor

class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = [
            'relation_with_customer', 
            'name', 
            'dob', 
            'gender', 
            'email', 
            'address', 
            'city', 
            'state', 
            'country', 
            'pin_code', 
            'mobile', 
            'photo', 
            'profession', 
            'income_certificate', 
            'bank_name', 
            'current_account_no', 
            'passbook_copy', 
            'ifsc_code'
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    guarantors = GuarantorSerializer(many=True)  

    class Meta:
        model = Application
        fields = [
            'aadhaar_no', 
            'pan_no', 
            'type_of_employment', 
            'business_title', 
            'business_type', 
            'business_address', 
            'gst_registration_no', 
            'business_license_no', 
            'expected_average_annual_turnover', 
            'years_in_current_business', 
            'collateral', 
            'status', 
            'application_timestamp', 
            'remark', 
            'credit_score', 
            'guarantors'  
        ]
