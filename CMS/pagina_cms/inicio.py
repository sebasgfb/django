from django.shortcuts import render, redirect
from .models import usuarios

def inicio(request):
    return render(request, 'inicio.html')

def acceder(request):
    if request.method == 'GET':
        if 'codigo_usuario' in request.session:
            variables = {}
            variables['nombre_usuario'] = request.session['nombre_usuario']
            return render(request, 'panel.html', variables)
        else:
            return render(request, 'acceder.html')
    
    if request.method == 'POST':
        v_usuario = request.POST.get('usuario')
        v_clave = request.POST.get('clave')
        verificar_usuario = usuarios.objects.filter(usuario=v_usuario, estado='ACTIVO')
        variables = {}
        if verificar_usuario.count() > 0:
            if verificar_usuario[0].clave == v_clave:
                request.session['codigo_usuario'] = verificar_usuario[0].id
                request.session['nombre_usuario'] = verificar_usuario[0].nombre
                request.session['nivel_usuario'] = verificar_usuario[0].nivel
                variables['nombre_usuario'] = request.session['nombre_usuario']

                # Redirigir según el nivel del usuario
                nivel_usuario = verificar_usuario[0].nivel
                if nivel_usuario == 'LECTOR':
                    return redirect('/ver_noticias')
                elif nivel_usuario in ['MODERADOR', 'ADMINISTRADOR']:
                    return redirect('/acceder')
                else:
                    # Manejar cualquier otro nivel no esperado
                    variables['m_error'] = 'Nivel de usuario no reconocido'
                    return render(request, 'acceder.html', variables)
            else:
                variables['m_error'] = 'La contraseña es incorrecta'
                return render(request, 'acceder.html', variables)
        else:
            variables['m_error'] = 'El usuario no está registrado'
            return render(request, 'acceder.html', variables)

def salir(request):
    if 'codigo_usuario' in request.session:
        del request.session['codigo_usuario']
    if 'nombre_usuario' in request.session:
        del request.session['nombre_usuario']
    if 'nivel_usuario' in request.session:
        del request.session['nivel_usuario']
    return redirect('inicio')
