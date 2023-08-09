from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
#all로 필드를 지정 시 db에서 자동으로 할당된 id값도 함께 가져올 수 있음.