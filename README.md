
# Sistema de Blog para Subir Noticias

Este proyecto es un sistema de blog en desarrollo que permite a los usuarios iniciar sesión y subir noticias. El sistema está diseñado para ser utilizado como una plataforma de publicación de noticias donde los usuarios pueden compartir información relevante con el público.

## Características

- **Inicio de Sesión de Usuarios:** Los usuarios pueden iniciar sesión para acceder al panel de control.
  
- **Panel de Control:** Una vez iniciada la sesión, los usuarios tienen acceso a un panel de control donde pueden realizar varias acciones, como agregar nuevas noticias, ver noticias existentes y administrar usuarios.

- **Agregar Noticias:** Los usuarios pueden agregar nuevas noticias proporcionando un título, contenido y posiblemente una imagen destacada.

- **Ver Noticias:** Los usuarios pueden ver todas las noticias existentes en el sistema, incluidos los títulos y fragmentos de contenido.

- **Administrar Usuarios:** Los usuarios con privilegios administrativos pueden administrar otros usuarios, como crear nuevos usuarios, eliminar usuarios o cambiar sus permisos.

## Tecnologías Utilizadas

- **Django:** El proyecto utiliza el framework web Django de Python para la lógica del servidor y la gestión de la base de datos.

- **HTML/CSS/Bootstrap:** Para la estructura y el diseño de las páginas web, se utilizan HTML, CSS y el framework de front-end Bootstrap para una apariencia más atractiva y responsiva.

- **JavaScript/jQuery:** Se emplea JavaScript y la biblioteca jQuery para la interactividad de la interfaz de usuario.

## Instalación

1. Clona el repositorio a tu máquina local:

```bash
git clone https://github.com/tu_usuario/sistema-blog.git
```

2. Instala las dependencias del proyecto:

```bash
cd sistema-blog
pip install -r requirements.txt
```

3. Configura la base de datos según las especificaciones de tu entorno.

4. Ejecuta las migraciones para crear las tablas necesarias en la base de datos:

```bash
python manage.py migrate
```

5. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abre tu navegador web y visita `http://localhost:8000` para acceder al sistema de blog.

## Contribución

Si deseas contribuir al desarrollo de este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit de ellos (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push de tu rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request.

---
