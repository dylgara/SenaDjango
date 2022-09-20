from ast import If
from curses.ascii import HT
from pickletools import read_uint1
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#Mensajes tipo cookie temporales
from django.contrib import messages


#Gestion de errores de bases de datos
from django.db import IntegrityError

from .models import Trabajador,Categoria,Produccion,Producto

# Create your views here.
def index(request):
    return render(request, 'planta/index.html')

def listarTrabajador(request):
    q = Trabajador.objects.all()
    contexto = {"datos": q}
    return render(request, 'planta/trabajador/listar_trabajador.html', contexto)

def formularioTrabajador(request):
    return render(request, 'planta/trabajador/nuevo_trabajador.html')

def guardarTrabajador(request):
    try:
        if request.method == "POST":
            q = Trabajador(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                correo = request.POST["correo"]
            )
            q.save()
            messages.success(request, "Trabajador guardado correctamente")
            messages.infor(request, "aaaaaaaaaa")
            messages.warning(request, "bbbbbbbbb")
            messages.error(request, "ccccccc")
            messages.debug(request, "ddddddd")
        else:
            messages.warning(request, "Usted no ha enviado datos...")
    except Exception as e:
        messages.success(request, f"Error: {e}")
    return redirect('planta:listarTrabajador')

def listarProducto(request):
    q = Producto.objects.all()
    contexto = {"datos": q}
    return render(request, 'planta/producto/listar_producto.html', contexto)

def formularioProducto(request):
    q = Categoria.objects.all()
    contexto = { "cat": q }
    return render(request, 'planta/producto/nuevo_producto.html', contexto)

def guardarProducto(request):
    try:
        if request.method == "POST":
            c = Categoria.objects.get(pk = request.POST["categoria"])
            q = Producto(
                nombre = request.POST["nombre"],
                ficha_tecnica = request.POST["ficha_tecnica"],
                costo = request.POST["costo"],
                categoria = c,
                color= request.POST["color"]
            )
            q.save()
            messages.success(request, "Producto guardado correctamente")
        else:
            messages.warning(request, "Usted no ha enviado datos...")
    except Exception as e:
        messages.success(request, f"Error: {e}")
    return redirect('planta:listarProducto')

def formularioEditar(request, id):
    p = Producto.objects.get(pk=id)
    q = Categoria.objects.all()
    contexto = { "cat": q, "producto": p }
    return render(request, 'planta/producto/editar_producto.html', contexto)


def actualizarProducto(request):
    try:
        if request.method == "POST":
            p = Producto.objects.get(pk = request.POST["id"])
            c = Categoria.objects.get(pk = request.POST["categoria"])
            
            p.nombre = request.POST["nombre"]
            p.ficha_tecnica = request.POST["ficha_tecnica"]
            p.costo = request.POST["costo"]
            p.categoria = c
            p.color= request.POST["color"]
            
            p.save()
            messages.success(request, "Producto actualizado correctamente")
        else:
            messages.warning(request, "Usted no ha enviado datos...")
    except Exception as e:
        messages.success(request, f"Error: {e}")
    return redirect('planta:listarProducto')

def eliminarProducto(request, id):
    try:
        p = Producto.objects.get(pk = id)
        p.delete()
        messages.success(request, "Producto eliminado correctamente!")
    except IntegrityError:
        messages.warning(request, "No puede eliminar este producto por que otros registros estan relacionados con el...")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    
    return redirect('planta:listarProducto')