from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.models import User
from .serializers import UserSerializer
from .serializers import RegistrationSerializer
from .serializers import LoginSerializer
from .serializers import TokenSerializer
from .serializers import LogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
#from .serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
import bcrypt 

@api_view(['POST'])
def create_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_data = {'username': serializer.validated_data['username']}
        return Response(response_data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_user(request,uid):
    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        return Response(status = 404)
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']

    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token

    return Response({'refresh': str(refresh), 'access': str(access_token)}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def logout_view(request):
    serializer = LogoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        refresh_token = serializer.validated_data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)