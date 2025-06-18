from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Book
        fields = ['id','title','price','author','author_username']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True,required=True,label='确认密码')

    class Meta:
        model = User
        fields = ['username','email','password','password2','email','first_name','last_name']
        extra_kwargs = {'email':{'required':True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "密码不一致"})
        return attrs

    def create(self, validated_data:dict):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
            password=validated_data['password']
        )
        # user.set_password(validated_data['password'])
        # user.save()
        return user