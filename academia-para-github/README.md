# Sistema de Gestión Académica (academia)

Proyecto Django con arquitectura MVT: cursos, profesores y estudiantes, con
autenticación por sesiones, mensajes flash y paginación (Bootstrap 5).

## Cómo ejecutarlo (Windows / PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Rutas principales: `/web/cursos/`, `/profesores/`, `/web/estudiantes/`,
`/accounts/login/` y `/admin/`.
