from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from favorite.models import FavoriteItems
from favorite.serializers import FavorSerializer


class FavoriteItemsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        favoritem = FavoriteItems.objects.filter(user=user)
        serializer = FavorSerializer(favoritem, many=True)
        return Response(serializer.data)

class CreateFavoriteView(CreateAPIView):
    serializer_class = FavorSerializer
    permission_classes = [IsAuthenticated]
