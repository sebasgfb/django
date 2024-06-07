from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from .serializador import SerialComentarios, SerialGrupos, SerialNoticias, SerialDetallesNoticias, SerialUsuarios
from .models import comentarios, grupos, noticias, usuarios
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response 

class ComentariosAPILista(generics.ListAPIView):
    serializer_class = SerialComentarios

    def get_queryset(self):
        noticia_id = self.request.query_params.get('noticia', None)
        if noticia_id is not None:
            queryset = comentarios.objects.filter(noticia_id=noticia_id).select_related('noticia')  # Ejemplo con select_related
        else:
            queryset = comentarios.objects.all().select_related('noticia')
        return queryset

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

class GruposAPIBorrar(generics.DestroyAPIView):
    lookup_field='id'
    queryset=grupos.objects.all()