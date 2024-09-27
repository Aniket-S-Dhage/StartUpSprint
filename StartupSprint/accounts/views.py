from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from .models import User
from django.utils.crypto import get_random_string
from rest_framework import generics
from .serializers import UserSerializer

@csrf_exempt
def register_user(request):
    
    if request.method == 'POST':
        
        try:
            data = json.loads(request.body)
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            mobile = data.get('mobile')
            gender = data.get('gender')
            dob = data.get('dob')
            role = data.get('role')
            permanent_address = data.get('permanent_address')
            current_address = data.get('current_address')

            

            
            password = get_random_string(length=8)
                       
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile=mobile,
                gender=gender,
                dob=dob,
                role=role,
                permanent_address=permanent_address,
                current_address=current_address
            )
            user.set_password(password)
            user.save()
            
            try:
                send_mail(
                    subject = 'Account Registration - Your Credentials',
                    message = f'Hello {first_name},\n\nYour account has been created. Below are your login credentials:\n\nEmail: {email}\nPassword: {password}\n\nPlease log in and change your password.',
                    from_email=settings.EMAIL_HOST_USER,  
                    recipient_list=[email],
                    fail_silently=False,
                )
            
            except Exception as e:
                print(e)

            return JsonResponse({'message': 'User registered successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



class CustomerListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role='customer').prefetch_related('applications__guarantors','family','banks')
    






