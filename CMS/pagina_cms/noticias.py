from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import noticias, grupos, usuarios, comentarios
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
    grupo_id = request.GET.get('grupo')
    if grupo_id:
        vernoticias = noticias.objects.filter(grupo_id=grupo_id).order_by('-fecha')
    else:
        vernoticias = noticias.objects.all().order_by('-fecha')
    
    vergrupos = grupos.objects.all()
    return render(request, 'ver_noticias.html', {'noticias': vernoticias, 'grupos': vergrupos, 'grupo_seleccionado': grupo_id})


def ver_noticia_completa(request, noticia_id):
    noticia = get_object_or_404(noticias, id=noticia_id)
    nivel_usuario = request.session.get('nivel_usuario')

    if nivel_usuario == "LECTOR":
        comentarios_visibles = comentarios.objects.filter(noticia=noticia, visible=True).order_by('-fecha')
        comentarios_no_visibles = []
    elif nivel_usuario in ["ADMINISTRADOR", "MODERADOR"]:
        comentarios_visibles = comentarios.objects.filter(noticia=noticia, visible=True).order_by('-fecha')
        comentarios_no_visibles = comentarios.objects.filter(noticia=noticia, visible=False).order_by('-fecha')
    else:
        comentarios_visibles = []
        comentarios_no_visibles = []

    if request.method == 'POST':
        if nivel_usuario in ["ADMINISTRADOR", "LECTOR", "MODERADOR"]:
            cuerpo = request.POST.get('cuerpo')
            autor = usuarios.objects.get(nombre=request.session.get('nombre_usuario', ''))
            
            if nivel_usuario == "LECTOR":
                nuevo_comentario = comentarios(cuerpo=cuerpo, autor=autor, noticia=noticia, visible=False)
            else:  # ADMINISTRADOR or MODERADOR
                nuevo_comentario = comentarios(cuerpo=cuerpo, autor=autor, noticia=noticia, visible=True)
                
            nuevo_comentario.save()
            return redirect('ver_noticia_completa', noticia_id=noticia.id)

    return render(request, 'ver_noticia_completa.html', {
        'noticia': noticia,
        'nivel_usuario': nivel_usuario,
        'comentarios_visibles': comentarios_visibles,
        'comentarios_no_visibles': comentarios_no_visibles
    })


def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(comentarios, pk=comentario_id)
    if request.method == 'POST':
        if request.session.get('nivel_usuario') in ["ADMINISTRADOR", "MODERADOR"]:
            comentario.delete()
            messages.success(request, 'Comentario eliminado correctamente.')
        else:
            raise PermissionDenied
    return redirect('ver_noticia_completa', noticia_id=comentario.noticia.id)