from rest_framework import viewsets, generics
from times.serializers import campeonatoSerializer, timeSerializer, jogadorSerializer
from times.models import campeonato, time, jogador


class campeonatoViewSet(viewsets.ModelViewSet):
    queryset = campeonato.objects.all()
    serializer_class = campeonatoSerializer

class jogadorViewSet(viewsets.ModelViewSet):
    queryset = jogador.objects.all()
    serializer_class = jogadorSerializer


class timeViewSet(viewsets.ModelViewSet):
    queryset = time.objects.all()
    serializer_class = timeSerializer


