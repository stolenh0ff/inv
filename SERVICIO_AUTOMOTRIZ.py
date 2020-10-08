import os
import datetime
os.system('cls')

#VARIABLES NO RELEVANTES
nombre_clt = input("Ingrese su nombre: ").capitalize()
apelli_clt = input("Ingrese su apellido: ").capitalize()
rut_clt = int(input("Ingrese su rut (sin guion, ni puntos, si temina con k, reemplazelo con un 0): "))
marca_aut = input("Ingrese la marca de su vehículo: ").upper()
model_aut = input("Ingrese el modelo de su vehículo: ").capitalize()

rev_km = input("Desea que se realize la Revision 1000KM (2 Hrs): ").upper()

#VAR
separador = ("--------------------------------------------------------")
tiempo_total = 0
cant_serv = 0
estado_salida = False
formato_fecha = "%d/%m/%Y %H:%M"

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

#Variables del DATETIME

hr_entrega_llaves = datetime.datetime.now()
hr_entrega_llaves_formateada = hr_entrega_llaves.strftime(formato_fecha)
print(f"Hora de entrega de las llaves al servicio mecánico = {hr_entrega_llaves_formateada}")

hora_termina_servicio = hr_entrega_llaves + datetime.timedelta(minutes=tiempo_total)

hora_termina_servicio_formateada = hora_termina_servicio.strftime(formato_fecha)

if estado_salida == True:
    print(separador)
    print("SERVICIO AUTOMOTRIZ")
    print(separador)
    print("Cliente: " , nombre_clt, apelli_clt)
    print("Vehículo: " , marca_aut ,"|", model_aut)
    print("Servicios: " , servicios)
    print("Cantidad de servicios: " , cant_serv)
    print("Tiempo de espera: " , tiempo_total, "Minutos")
    print("Estado de los servicios: Inicializando")
    print(separador)
else:
    print("")

print("Seleccione lo que desea hacer: ")
print("(1) Consultar por el estado del servicio ")
accion = int(input("--->>> "))

reint_consulta = "SI"
while reint_consulta == "SI":
    if accion == 1:
        hr_pregunta_si_esta_listo = datetime.datetime.now()

        if hr_entrega_llaves <= hr_pregunta_si_esta_listo < hora_termina_servicio:
            print("El auto está en estado 'trabajando'")
            print(f"El auto se entregará en {tiempo_total} Minutos más, a las {hora_termina_servicio_formateada} hrs")
        if hr_pregunta_si_esta_listo == hora_termina_servicio:
            print("El auto está en estado 'terminado'")
        if hr_pregunta_si_esta_listo > hora_termina_servicio:
            print("El auto está en estado 'entregado'")
    reint_consulta = input("¿Desea volver a consultar? (SI/NO): ").upper()
#BenjaminSepulveda
