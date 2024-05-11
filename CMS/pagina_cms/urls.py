from django.urls import path
from . import inicio, usuarios, noticias, views

urlpatterns = [
    path('', inicio.inicio, name='inicio'),
    path('agregar_noticia', noticias.agregar_noticia, name='agregar_noticia'),
    path('eliminar_noticia/<int:noticia_id>/', noticias.eliminar_noticia, name='eliminar_noticia'),
    path('ver_noticias', noticias.ver_noticias, name='ver_noticias'),
    path('ver_noticia/<int:noticia_id>/', noticias.ver_noticia_completa, name='ver_noticia_completa'),
    path('verusuario', usuarios.ver, name='verusuario'),
    path('nueusuario', usuarios.nuevo, name='nueusuario'),
    path('modusuario/<id>', usuarios.modificar, name='modusuario'),
    path('borusuario/<id>', usuarios.borrar, name='borusuario'),
    path('acceder', inicio.acceder, name='acceder'),
    path('salir', inicio.salir, name='salir'),
    path('listanoticias', views.NoticiasAPILista.as_view(), name='listanoticias'),
    path('listanoticias/<int:id>', views.NoticiasAPIDetalle.as_view(), name='detallenoticias')
]