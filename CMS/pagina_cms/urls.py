from django.urls import path
from . import inicio, usuarios, noticias, grupos, views

urlpatterns = [
    path('', inicio.inicio, name='inicio'),
    path('agregar_noticia', noticias.agregar_noticia, name='agregar_noticia'),
    path('eliminar_noticia/<int:noticia_id>/', noticias.eliminar_noticia, name='eliminar_noticia'),
    path('ver_noticias', noticias.ver_noticias, name='ver_noticias'),
    path('ver_grupos', grupos.ver_grupos, name='ver_grupos'),
    path('agregar_grupo', grupos.agregar_grupo, name='agregar_grupo'),
    path('eliminar_grupo/<int:grupo_id>/', grupos.eliminar_grupo, name='eliminar_grupo'),  
    path('ver_noticia/<int:noticia_id>/', noticias.ver_noticia_completa, name='ver_noticia_completa'),
    path('eliminar_comentario/<int:comentario_id>/', noticias.eliminar_comentario, name='eliminar_comentario'),
    path('aprobar_comentario/<int:comentario_id>/', noticias.aprobar_comentario, name='aprobar_comentario'),
    path('verusuario', usuarios.ver, name='verusuario'),
    path('nueusuario', usuarios.nuevo, name='nueusuario'),
    path('modusuario/<id>', usuarios.modificar, name='modusuario'),
    path('borusuario/<id>', usuarios.borrar, name='borusuario'),
    path('acceder', inicio.acceder, name='acceder'),
    path('salir', inicio.salir, name='salir'),
    path('listanoticias', views.NoticiasAPILista.as_view(), name='listanoticias'),
    path('listanoticias/<int:id>', views.NoticiasAPIDetalle.as_view(), name='detallenoticias')
]