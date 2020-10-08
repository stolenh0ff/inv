import os
from random import randint
os.system('cls')

#VARIABLES NO RELEVANTES
nombre_clt = input("Ingrese su nombre: ")
apelli_clt = input("Ingrese su apellido: ")
rut_clt = int(input("Ingrese su rut (sin guion, ni puntos, si temina con k, reemplazelo con un 0): "))
marca_aut = input("Ingrese la marca de su vehículo: ").upper()
model_aut = input("Ingrese el modelo de su vehículo: ")

rev_km = input("Desea que se realize la Revision 1000KM (2 Hrs): ").upper()

#SERVICIOS SOLICITADOS

#SERVICIO OPCIONAL
#Lavado de auto

#VAR
separador = ("--------------------------------------------------------")
tiempo_total = 0
cant_serv = 0
estado_salida = False
estado_s = ["Trabajando", "Terminado", "Entregado"]

servicios = ""

tiempo_total = 0
cant_serv = 0

if rev_km == "SI":
    tiempo_total = tiempo_total + 120
    cant_serv = cant_serv + 1
    cam_aceite = input("Desea que se realize el Cambio de Aceite (1 Hr): ").upper()
    servicios = servicios + "Revision 1000KM | "
elif rev_km == "NO":
    cam_aceite = input("Desea que se realize el Cambio de Aceite (1 Hr): ").upper()

if cam_aceite == "SI":
    tiempo_total = tiempo_total + 60
    cant_serv = cant_serv + 1
    rev_frenos = input("Desea que se realize la Revision a los Frenos (30 Minutos): ").upper()
    servicios = servicios + "Cambio de Aceite | "
elif cam_aceite == "NO":
    rev_frenos = input("Desea que se realize la Revision a los Frenos (30 Minutos): ").upper()

if rev_frenos == "SI":
    tiempo_total = tiempo_total + 30
    cant_serv = cant_serv + 1
    rev_correas = input("Desea que se realize la Revision a las Correas (30 Minutos): ").upper()
    servicios = servicios + "Revision de frenos | "
elif rev_frenos == "NO": 
    rev_correas = input("Desea que se realize la Revision a las Correas (30 Minutos): ").upper()

if rev_correas == "SI":
    tiempo_total = tiempo_total + 30
    cant_serv = cant_serv + 1
    rev_luces = input("Desea que se realize la Revision de las Luces (12 Minutos): ").upper()
    servicios = servicios + "Revision Correas | "
elif rev_correas == "NO":
    rev_luces = input("Desea que se realize la Revision de las Luces (12 Minutos): ").upper()

if rev_luces == "SI":
    tiempo_total = tiempo_total + 12
    cant_serv = cant_serv + 1
    rev_direc = input("Desea que se realize la Revision a la Dirección (30 Minutos): ").upper()
    servicios = servicios + "Revision de luces | "
elif rev_luces == "NO":
    rev_direc = input("Desea que se realize la Revision a la Dirección (30 Minutos): ").upper()

if rev_direc == "SI":
    tiempo_total = tiempo_total + 30
    cant_serv = cant_serv + 1
    lavar_auto = input("¿Desea el lavado adicional gratuito para el vehiculo? (Se demorará 30 Minutos adicionales): ").upper()
    servicios = servicios + "Revision de direccion | "
elif rev_direc == "NO":
    lavar_auto = input("¿Desea el lavado adicional gratuito para el vehiculo? (Se demorará 30 Minutos adicionales): ").upper()

if lavar_auto == "SI":
    tiempo_total = tiempo_total + 30
    cant_serv = cant_serv + 1
    servicios = servicios + "Lavado del vehículo | "
    estado_salida = True
elif lavar_auto == "NO":
    estado_salida = True

if estado_salida == True:
    print(separador)
    print("SERVICIO AUTOMOTRIZ")
    print(separador)
    print("Cliente: " , nombre_clt, apelli_clt)
    print("Vehículo: " , marca_aut ,"|", model_aut)
    print("Servicios: " , servicios)
    print("Cantidad de servicios: " , cant_serv)
    print("Tiempo de espera: " , tiempo_total, "Minutos")
    print("Estado de los servicios: " , estado_s[randint(0,2)])
    print(separador)
else:
    print("")
