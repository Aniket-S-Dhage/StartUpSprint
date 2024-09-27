from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework import status ,generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.conf import settings
from customer.models import Bank
from .serializers import BankSerializer
from rest_framework.exceptions import ValidationError
import requests
from customer.serializers import FamilySerializer
from customer.models import Family


class ApplicationCreateView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data, context={'request': request})
        
        if not request.user.is_authenticated:  
            return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            
            obj = serializer.save()
            
            send_mail(
                'Application Created Successfully',
                f'Your Application ID is : {obj.id} Use this ID to Track Your Application Status',
                settings.DEFAULT_FROM_EMAIL, 
                [obj.user.email],
                fail_silently=False,
            ) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ApplicationStatusView(APIView):

    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]

    def get(self, request, id, *args, **kwargs):
    
        try:   
            application = Application.objects.get(id=id, user=request.user)
          
            return Response({'status': application.status}, status=status.HTTP_200_OK)
        except Application.DoesNotExist:
            
            return Response({'detail': 'Application ID not found.'}, status=status.HTTP_404_NOT_FOUND)





class BankDetailsView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        ifsc_code = kwargs.get('ifsc_code', None)

        if ifsc_code:
            try:
                response = requests.get(f'https://ifsc.razorpay.com/{ifsc_code}')
                if response.status_code == 200:
                    bank_data = response.json()
                    return Response({
                        'BANK': bank_data.get('BANK'),
                        'ADDRESS': bank_data.get('ADDRESS')
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid IFSC code."}, status=status.HTTP_404_NOT_FOUND)
            except requests.exceptions.RequestException:
                return Response({"error": "Unable to fetch bank details."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        ifsc_code = request.data.get('ifsc_code')

        try:
            response = requests.get(f'https://ifsc.razorpay.com/{ifsc_code}')
            if response.status_code == 200:
                bank_data = response.json()
                
                
                data_with_user = request.data.copy()
                data_with_user['user'] = request.user.id 
                
                serializer = self.get_serializer(data=data_with_user)
                serializer.is_valid(raise_exception=True)

               
                serializer.save(
                    bank_name=bank_data.get('BANK'),
                    bank_address=bank_data.get('ADDRESS')
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Invalid IFSC code."}, status=status.HTTP_404_NOT_FOUND)
        except requests.exceptions.RequestException:
            return Response({"error": "Unable to fetch bank details."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        user = request.user
        
       
        family_members = Family.objects.filter(user=user)
        bank_details = Bank.objects.filter(user=user)
        applications = Application.objects.filter(user=user)
        
        # Serialize the data
        family_data = FamilySerializer(family_members, many=True).data
        bank_data = BankSerializer(bank_details, many=True).data
        application_data = ApplicationSerializer(applications, many=True).data

        # Return combined response
        return Response({
            'family_info': family_data,
            'bank_info': bank_data,
            'application_info': application_data
        }, status=status.HTTP_200_OK)




