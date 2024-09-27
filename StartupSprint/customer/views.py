from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from customer.models import Enquiry
from .serializers import EnquirySerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.response import Response
from .models import Family
from .serializers import FamilySerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Family
from .serializers import FamilySerializer


class EnquiryCreateView(APIView):
    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            
            enquiry = serializer.save()

            send_mail(
                'Enquiry Received',
                f'Your enquiry has been received. Your enquiry ID is: {enquiry.id}',
                settings.DEFAULT_FROM_EMAIL, 
                [enquiry.email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EnquiryStatusView(APIView):
    def get(self, request, pk):
        email = request.query_params.get('email')
        
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            enquiry = Enquiry.objects.get(id=pk)       
            if enquiry.email != email:
                return Response({'error': 'Email does not match the provided Enquiry ID.'}, status=status.HTTP_400_BAD_REQUEST)  
            return Response({'status': enquiry.status}, status=status.HTTP_200_OK)
        
        except Enquiry.DoesNotExist:     
            return Response({'error': 'Enquiry ID not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e: 
            return Response({'error': f'Internal server error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







class FamilyDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = FamilySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        user = self.request.user
        try:
           
            return Family.objects.get(user=user)
        except Family.DoesNotExist:
            
            raise NotFound("Family details not found for this user.")

    def get(self, request, *args, **kwargs):
      
        try:
            family_details = self.get_object()
            serializer = self.get_serializer(family_details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            
            return Response({"detail": "Family details not found. You can create new details."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        
        try:
            family_details = self.get_object()
            serializer = self.get_serializer(family_details, data=request.data, partial=True)
        except NotFound:
           
            serializer = self.get_serializer(data=request.data)

       
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)







