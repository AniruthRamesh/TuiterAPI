from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweets_app.models import Tuit
from .serializers import TuitSerializer

@api_view(['GET'])
def find_tuits(request):
    tuits = Tuit.objects.all()
    serializer = TuitSerializer(tuits, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_tuit(request):
    serializer = TuitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_tuit(request, tid):
    try:
        tuit = Tuit.objects.get(id=tid)
    except Tuit.DoesNotExist:
        return Response(status=404)
    serializer = TuitSerializer(tuit, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_tuit(request, tid):
    try:
        tuit = Tuit.objects.get(id=tid)
    except Tuit.DoesNotExist:
        return Response(status=404)
    tuit.delete()
    return Response(status=204)
