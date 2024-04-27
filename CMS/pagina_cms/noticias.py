from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import noticias, grupos, usuarios
from django.core.exceptions import PermissionDenied


def agregar_noticia(request):
    if request.method == 'GET':
        if 'nivel_usuario' in request.session and request.session['nivel_usuario'] == 'ADMINISTRADOR' or request.session['nivel_usuario'] == 'MODERADOR':
            vergrupos = grupos.objects.all()
            return render(request, 'agregar_noticia.html', {'grupos': vergrupos})
        else:
            variables = {
                'm_error': 'No tiene permisos para agregar noticias.',
                'nombre_usuario': request.session.get('nombre_usuario', '')
            }
            return render(request, 'panel.html', variables)

    if request.method == 'POST':
        ntitulo = request.POST.get('titulo')
        ncuerpo = request.POST.get('cuerpo')
        nimagen = request.FILES.get('imagen') 
        ngrupo_id = request.POST.get('grupo')
        nautor, created = usuarios.objects.get_or_create(nombre=request.session.get('nombre_usuario', ''), defaults={'nombre': request.session.get('nombre_usuario', '')})

        ngrupo = grupos.objects.get(id=ngrupo_id)

        noticia = noticias(titulo=ntitulo, cuerpo=ncuerpo, imagen=nimagen, grupo=ngrupo, autor=nautor)
        noticia.save()
        
        messages.success(request, 'Noticia agregada correctamente.')
        
        return redirect('ver_noticias')

def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(noticias, pk=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, 'Noticia eliminada correctamente.')
    return redirect('ver_noticias')

def ver_noticias(request):
    vernoticias = noticias.objects.all().order_by('-fecha')
    nivel_usuario = None
    if 'nivel_usuario' in request.session:
        nivel_usuario = request.session['nivel_usuario']
    return render(request, 'ver_noticias.html', {'noticias': vernoticias, 'nivel_usuario': nivel_usuario})
