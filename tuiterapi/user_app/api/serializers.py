from rest_framework import serializers
from user_app.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import bcrypt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def save(self):
        if User.objects.filter(email =self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        if User.objects.filter(username =self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'username already exists'})
        
        password = self.validated_data['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        account = User(email=self.validated_data['email'], username=self.validated_data['username'], password=hashed_password)
        account.save()

        return account
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            stored_password = user.password

            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                attrs['user'] = user
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        except User.DoesNotExist:
            raise serializers.ValidationError('Unable to log in with provided credentials.')

        return attrs


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()

    def create(self, validated_data):
        return RefreshToken(**validated_data)

    def to_representation(self, instance):
        return {
            'refresh': str(instance),
            'access': str(instance.access_token),
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        try:
            refresh_token = RefreshToken(attrs['refresh'])
            attrs['refresh_token'] = refresh_token
        except Exception as e:
            raise serializers.ValidationError('Invalid token.')

        return attrs