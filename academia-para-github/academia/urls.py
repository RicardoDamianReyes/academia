from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cursos.views import LoginBienvenidaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cursos.urls')),

    # Rutas nativas de autenticación de Django
    path('accounts/login/', LoginBienvenidaView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]