
from django.contrib import admin
from django.urls import path
from CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('editar/<cedula>', views.editar),
    path('editar_persona/', views.edit_persona),
    path('ingresar/', views.registro_personas),
    path('eliminar/<int:id>', views.Eliminar)

]
