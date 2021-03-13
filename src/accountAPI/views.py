from django.shortcuts import render
from accountAPI.serializers import RegistrationSerializer
from account.models import Account


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes



@api_view(['POST'])
def UserRegistration(request):
    data = {}
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data['email'] = user.email
        data['username'] = user.username
        data['response'] = 'Successfully registerd'
        return Response(data)
    
        
