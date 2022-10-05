from django.shortcuts import render, redirect
from CRUD.models import Personas



def Home(request):
    content = {
        'titulo': 'CRUD',
        'post': Personas.objects.all()
    }
    return render(request, 'datos.html', content)


def Eliminar(request, id):
    persona = Personas.objects.get(id=id)
    persona.delete()
    return redirect('/')


def registro_personas(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    edad = request.POST['edad']
    emial = request.POST['email']
    telefono = request.POST['telefono']
    cedula = request.POST['cedula']

    personas = Personas.objects.create(
        nombre=nombre, apellido=apellido, edad=edad, email=emial, telefono=telefono, cedula=cedula)
    return redirect('/')


def editar(request, cedula):
    persona = Personas.objects.get(cedula=cedula)
    return render(request, 'editar.html', {'persona': persona})


def edit_persona(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    edad = request.POST['edad']
    emial = request.POST['email']
    telefono = request.POST['telefono']
    cedula = request.POST['cedula']

    persona = Personas.objects.get(cedula=cedula)
# * esto sirve para modificar  datos en la base de datos desde el frontend
    persona.nombre = nombre
    persona.apellido = apellido
    persona.edad = edad
    persona.email = emial
    persona.telefono = telefono
    # persona.cedula = cedula
    persona.save()

    return redirect('/')
