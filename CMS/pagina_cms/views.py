from django.shortcuts import render
from rest_framework import generics
from .serializador import SerialNoticias, SerialDetallesNoticias
from .models import noticias

# Create your views here.
class NoticiasAPILista(generics.ListAPIView):
    queryset=noticias.objects.all()
    serializer_class=SerialNoticias

class NoticiasAPIDetalle(generics.RetrieveAPIView):
    lookup_field='id'
    queryset=noticias.objects.all()
    serializer_class=SerialDetallesNoticias