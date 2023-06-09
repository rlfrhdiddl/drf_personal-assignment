from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        #create는 기본 내장 함수
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        #create는 기본 내장 함수지만 set_passsword를 해주기 위해 재정의
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username']= user.username
        token['gender']= user.gender
        token['age']= user.age
        return token