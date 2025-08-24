from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'confirm_password', 
                 'bio', 'profile_picture', 'followers', 'token')
        read_only_fields = ('followers', 'token')

    def get_token(self, obj):
        # Delete existing token if it exists
        Token.objects.filter(user=obj).delete()
        # Create new token
        token = Token.objects.create(user=obj)
        return token.key

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})