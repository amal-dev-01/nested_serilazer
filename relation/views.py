from django.shortcuts import render

# Create your views here.
from relation.serializers import SingerSerializer,SongSerializer
from rest_framework import viewsets
from relation.models import Singer,Song


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer