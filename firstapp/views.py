from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

import os

# Create your views here.
@api_view(['POST'])
def signup_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        age = request.data.get('age')
        photo = request.FILES.get('photo')
        
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        relative_file_path = filename
        uploaded_file_path = fs.path(filename)
        #업로드된 파일이 실제 저장된 경로
        
        static_file_path = os.path.join(settings.MEDIA_ROOT, filename)
        #장고에서 정의한 미디어 파일의 경로
        
        os.rename(uploaded_file_path, static_file_path)
        #앞 인자--->뒤 인자로 변경
        
        user = User.objects.create(username = username, age = age, photo = relative_file_path)
        
        serializer = UserSerializer(user)
        serializer_data = serializer.data
        #serializer의 .data를 응답으로 줘야함
        
        return Response(serializer_data)
    
@api_view(['GET'])
def listAPI(request):
        if request.method == "GET":
            users = User.objects.all()
            serializer = UserSerializer(users, many = True)
            serializer_data = serializer.data
        return Response(serializer_data)
    
@api_view(['GET'])
def user_detail(request, userId):
        try:
            print(userId)
            user = User.objects.get(id = userId)
            serializer = UserSerializer(user)
            
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        


