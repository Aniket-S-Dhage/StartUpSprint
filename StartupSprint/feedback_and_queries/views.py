from rest_framework.response import Response
from feedback_and_queries.models import FeedBack
from feedback_and_queries.serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

class FeedbackView(APIView):
    def post(self,request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save()
            send_mail(
            subject="StartupSprint Feedback Mail",
            message="Thank you, Your feedback submitted successfully!!!",
            from_email= settings.EMAIL_HOST_USER ,
            recipient_list=[ obj.email ],
            fail_silently=False
        )
            return Response({'msg':'Your Feedback submitted successfully', 
            'status':'success', 'feedback':serializer.data},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors) 


    def get(self,request, format=None):    
        feedback = FeedBack.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response({'msg':'Your Feedback submitted successfully', 
            'status':'success', 'feedback':serializer.data},
            status=status.HTTP_200_OK)
    

