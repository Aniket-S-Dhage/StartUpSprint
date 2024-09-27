from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Application
from customer.models import Bank
import re


User = get_user_model() 

class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Application
        fields = "__all__"

    def validate_aadhaar_no(self, value):
        if not value.isdigit() or len(value) != 12:
            raise serializers.ValidationError("Aadhaar number must be 12 digits.")
        return value

    def validate_pan_no(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("PAN number must be exactly 10 characters.")
        return value

   
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user 
        return super().create(validated_data)




class BankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bank
        fields = ['user', 'bank_name', 'account_number', 'ifsc_code', 'passbook_copy', 'bank_address']

    def validate_ifsc_code(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("IFSC code must be 11 characters.")
        return value

    


