from rest_framework import serializers
from .models import noticias

class SerialNoticias(serializers.ModelSerializer):
    class Meta:
        model=noticias
        fields= [
            'id',
            'titulo',
            'fecha',
            'cuerpo',
            'imagen',
        ]

class SerialDetallesNoticias(serializers.ModelSerializer):
    class Meta:
        model=noticias
        fields= [
            'id',
            'titulo',
            'fecha',
            'imagen',
            'cuerpo',
            'autor',
        ]