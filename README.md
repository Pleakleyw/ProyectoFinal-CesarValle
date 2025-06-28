# 🥗 Delicior - Recetario web con Django

**Delicior** es una aplicación web desarrollada con Django que permite a los usuarios crear, compartir, explorar y comentar recetas caseras. Su diseño modular permite una navegación fluida, uso seguro de autenticación y una experiencia visual cuidada con Bootstrap 5.

---

## 🚀 Características principales

- Registro e inicio de sesión de usuarios  
- CRUD completo de recetas (crear, editar, eliminar, listar)  
- Sistema de comentarios por receta  
- Filtros por categoría de receta  
- Paginación automática (12 recetas por página)  
- Carga de imágenes para cada receta  
- Slug generado automáticamente  
- Vista `/about/` con información del autor  
- Navegación dinámica con barra de menú  
- Seguridad por roles:  
  - Solo el autor puede modificar o eliminar su receta  
  - El administrador (superuser) puede modificar o eliminar cualquier receta desde la web  
- Interfaz responsive con Bootstrap 5  

---

## 🛠️ Tecnologías utilizadas

- Python 3.11  
- Django 4.x  
- SQLite3 (modo desarrollo)  
- Bootstrap 5  
- CKEditor (texto enriquecido)  
- Widget Tweaks  
- FontAwesome & Bootstrap Icons  

---

## 📂 Estructura del proyecto

```bash
Recetario/
├── accounts/         # Gestión de usuarios (registro, perfil)
├── recetas/          # App principal: modelos y vistas de recetas
├── pages/            # Home y página about
├── templates/        # HTML organizados por app
├── media/            # Imágenes subidas
├── static/           # Archivos CSS/JS e imágenes estáticas
├── manage.py
├── requirements.txt
└── README.md
```
## 👤 Autor

- **Nombre:** Cesar Jordan Valle Yataco

---

## 🔑 Usuario demo

Para efectos de prueba, puedes iniciar sesión como administrador utilizando las siguientes credenciales.
Con este acceso podrás visualizar los datos almacenados en la base de datos desde la interfaz web, así como editar y eliminar cualquier receta directamente desde la plataforma:

- **Usuario:** `wanakin`  
- **Contraseña:** `123456`
