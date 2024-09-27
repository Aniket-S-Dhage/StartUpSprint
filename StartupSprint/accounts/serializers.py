from rest_framework import serializers
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from customer.serializers import BankSerializer,FamilySerializer
from application_generation.serializers import ApplicationSerializer
from .models import User  

class UserSerializer(serializers.ModelSerializer):

    applications = ApplicationSerializer(many=True)
    family = FamilySerializer()  
    banks = BankSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'dob', 'gender',
            'permanent_address', 'current_address', 'mobile', 
            'photo', 'signature', 'role', 'is_active_models','applications','family','banks'
        ]

    def create(self, validated_data):
        role = validated_data.get('role')
        email = validated_data.get('email')

       
        random_password = AbstractBaseUser().make_random_password()

        
        user = User.objects.create(
            email=email,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            role=role,
            password=make_password(random_password),
        )

        
        return user, random_password