# accounts/serializers.py

from rest_framework import serializers
from .models import Users

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'handle', 'first_name', 'password', 'last_name', 'country_calling_code', 'phone_number', 'role', 'organisation')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        print(validated_data)
        user = Users(
            email=validated_data['email'],
            handle=validated_data['handle'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            country_calling_code=validated_data.get('country_calling_code', ''),
            phone_number=validated_data.get('phone_number', ''),
            role=validated_data.get('role'),
            organisation=validated_data.get('organisation'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
