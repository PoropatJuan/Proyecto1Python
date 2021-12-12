from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

#Paso 1

from django.template import loader

def saludo(request):   #Primera Vista
	return HttpResponse("Hola Juani y Django - Coder")

def segundaVista(request):   #Segunda Vista
	return HttpResponse("Segunda Vista Activa")

def dia(request):   #Tercera Vista
	
    variable = datetime.now()
    
    return HttpResponse(f"hoy es un gran día <br> {variable}")

def apellido(request, ape):   #Quinta Vista

    fecha = datetime.now()
    return HttpResponse(f"El profe de coder {ape} es muy bueno..<br><br>.. Por lo menos hoy {fecha}")

def probandoTemplate(request):   #Sexta Vista

    mejorEstudiante = "Poropat Juan"
    nota = 8.9
    fecha = datetime.now()
    estudiantesMasSimpaticos = ["juanse", "nadia", "cristo"]
    dicc = {"nombre": mejorEstudiante, "nota": nota, "fecha": fecha, "estudiantes":estudiantesMasSimpaticos}

#Paso 3
    plantilla = loader.get_template("template1.html")


    #miHTML = open("C:/Users/Poro/Desktop/PYTHON/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHTML.read())
    #miHTML.close()

    #miContexto = Context()

    #documento = plantilla.render(miContexto)
    documento = plantilla.render(dicc)

    return HttpResponse(documento)

    a