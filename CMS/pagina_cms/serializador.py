from rest_framework import serializers
from .models import grupos, noticias, usuarios

class SerialUsuarios(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = [
            'id',
            'nombre',
            'usuario',
            'clave',
            'estado',
            'nivel',
        ]

class SerialNoticias(serializers.ModelSerializer):
    class Meta:
        model=noticias
        fields= [
            'id',
            'titulo',
            'grupo',
            'fecha',
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
            'grupo',
            'autor',
        ]

class SerialGrupos(serializers.ModelSerializer):
    class Meta:
        model=grupos
        fields=[
            'id',
            'grupo',
        ]