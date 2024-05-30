from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import noticias, grupos, usuarios, comentarios
from django.core.exceptions import PermissionDenied

def ver_grupos(request):
    if request.method == 'GET':
        if 'nivel_usuario' in request.session and (request.session['nivel_usuario'] == 'ADMINISTRADOR' or request.session['nivel_usuario'] == 'MODERADOR'):
            vergrupos = grupos.objects.all()
            return render(request, 'ver_grupos.html', {'grupos': vergrupos})
        else:
            variables = {
                'm_error': 'No tiene permisos para administrar grupos.',
                'nombre_usuario': request.session.get('nombre_usuario', '')
            }
            return render(request, 'panel.html', variables)
    return render(request, 'ver_grupos.html')

def agregar_grupo(request):
    if request.method == 'POST':
        nombre_grupo = request.POST.get('nombre_grupo')
        grupo = grupos.objects.create(grupo=nombre_grupo)
        # Puedes agregar más lógica aquí si es necesario, como redireccionar a una página de éxito o validar datos
        return redirect('ver_grupos')
    return render(request, 'ver_grupos.html')

def eliminar_grupo(request, grupo_id):
    grupo = get_object_or_404(grupos, pk=grupo_id)
    if request.method == 'POST':
        grupo.delete()
        # Puedes agregar más lógica aquí si es necesario, como redireccionar a una página de éxito o validar datos
    return redirect('ver_grupos')
