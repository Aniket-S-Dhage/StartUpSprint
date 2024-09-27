from rest_framework import serializers
from customer.models import Enquiry
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Family

class EnquirySerializer(serializers.ModelSerializer):
   
    mobile = PhoneNumberField(region='IN', required=True)

    class Meta:
        model = Enquiry
        fields = '__all__'



    def validate_first_name(self, fname):

        if len(fname) < 2 :
            raise serializers.ValidationError("First name must have 2 charactors")
       
        if fname and not fname[0].isupper():
            raise serializers.ValidationError("The first letter of the first name must be capitalized.")
        return fname

   
    def validate_last_name(self, lname):

        if len(lname) < 2:
            raise serializers.ValidationError("The last name must be 2 charactors")
        
        if lname and not lname[0].isupper():
            raise serializers.ValidationError("The first letter of the last name must be capitalized.")
        return lname


    def validate_email(self, email):
       
        if not email.endswith(('@gmail.com', '@yahoo.com')):
            raise serializers.ValidationError("Email must be from the domain '@gmail.com' or @yahoo.com.")
        return email

   
    def validate(self, data):

      
        if len(data.get('message', '')) < 10:
            raise serializers.ValidationError({
                'message': "Message must be at least 10 characters long."
            })

        return data




class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = [
            'father_name', 'father_profession', 'father_income', 'father_contact',
            'mother_name', 'mother_profession', 'mother_income', 'mother_contact',
            'marital_status', 'spouse_name', 'spouse_income', 'spouse_profession',
            'spouse_contact'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        family, created = Family.objects.update_or_create(user=user, defaults=validated_data)
        return family

    def update(self, instance, validated_data):
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.father_profession = validated_data.get('father_profession', instance.father_profession)
        instance.father_income = validated_data.get('father_income', instance.father_income)
        instance.father_contact = validated_data.get('father_contact', instance.father_contact)
        instance.mother_name = validated_data.get('mother_name', instance.mother_name)
        instance.mother_profession = validated_data.get('mother_profession', instance.mother_profession)
        instance.mother_income = validated_data.get('mother_income', instance.mother_income)
        instance.mother_contact = validated_data.get('mother_contact', instance.mother_contact)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.spouse_name = validated_data.get('spouse_name', instance.spouse_name)
        instance.spouse_income = validated_data.get('spouse_income', instance.spouse_income)
        instance.spouse_profession = validated_data.get('spouse_profession', instance.spouse_profession)
        instance.spouse_contact = validated_data.get('spouse_contact', instance.spouse_contact)

        instance.save()
        return instance


        


