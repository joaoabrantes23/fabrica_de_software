from rest_framework import serializers
from times.models import campeonato, time, jogador


class campeonatoSerializer (serializers.ModelSerializer):
    class Meta:
        model = campeonato
        fields = '__all__'

class jogadorSerializer (serializers.ModelSerializer):
    class Meta:
        model = jogador
        fields = '__all__'

class timeSerializer (serializers.ModelSerializer):
    class Meta:
        model = time
        fields = '__all__'


