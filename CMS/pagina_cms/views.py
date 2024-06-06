from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from .serializador import SerialGrupos, SerialNoticias, SerialDetallesNoticias, SerialUsuarios
from .models import grupos, noticias, usuarios
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response 

class UsuariosAPILista(generics.ListAPIView):
    queryset=usuarios.objects.all()
    serializer_class=SerialUsuarios

class NoticiasAPILista(generics.ListAPIView):
    queryset=noticias.objects.all()
    serializer_class=SerialNoticias

class NoticiasAPIDetalle(generics.RetrieveAPIView):
    lookup_field='id'
    queryset=noticias.objects.all()
    serializer_class=SerialDetallesNoticias

class GruposAPILista(generics.ListAPIView):
    queryset=grupos.objects.all()
    serializer_class=SerialGrupos

class GruposAPINuevo(generics.CreateAPIView):
    queryset=grupos.objects.all()
    serializer_class=SerialGrupos

class GruposAPIModificar(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset=grupos.objects.all()
    serializer_class=SerialGrupos

class GruposAPIBorrar(generics.DestroyAPIView):
    lookup_field='id'
    queryset=grupos.objects.all()