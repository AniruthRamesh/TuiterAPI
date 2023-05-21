from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.models import User
from .serializers import UserSerializer


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
    return Response(serializer.errors, status =400)

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