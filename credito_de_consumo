import os
os.system('cls')

#Variables

            #no relevantes
nombre = input("Ingrese su nombre: ")
addr = input("Ingrese su apellido: ")
rut = int(input("Ingrese su rut (sin guion ni puntos): "))


            #relevantes
edad = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese su sueldo mensual: "))
nacionalidad = input("Ingrese su nacionalidad: ").upper()
anostrab = int(input("Ingrese la cantidad de años que ha trabajado: "))
monto_s = int(input("Ingrese el monto a solicitar: "))
n_cuotas = int(input("Ingrese el numero de cuotas (entre 3 y 84 cuotas): "))

#Var

monto_s = int(monto_s)
n_cuotas = int(n_cuotas)
sueldo = int(sueldo)

moroso = 1

#calculo total

v_tasa = ( monto_s * 0.0146 )

v_cuota = (monto_s / n_cuotas)

v_total = ( ( v_cuota + v_tasa ) * n_cuotas )

#calculo monto maximo

m_max = (sueldo * 10)
m_max = int(m_max)

puede_sol_credito = False

mensaj_credito = ""

#edad
if edad >= 24 and edad <= 79:
    #sueldo
    if sueldo >= 300000:
        #nacionalidad
        if nacionalidad == "CHILENO" or nacionalidad == "CHILENA":
             #antiguedad laboral
            if anostrab >= 3:
                #solicituddinero
                if monto_s >= 500000:
                    #cantidad de cuotas
                    if n_cuotas >= 3 or n_cuotas <=84:
                        if moroso == 1:
                            puede_sol_credito = True
                        else:
                            mensaj_credito = "***Deudor moroso***"
                    else:
                        mensaj_credito = "***Numero de cuotas no corresponde***"
                else:
                    mensaj_credito = "***El valor debe ser igual o superior a 500000***"
            else: 
                mensaj_credito = "***Debe haber trabajado 3 o más años***" 
        else:
            mensaj_credito = "***Debe ser poseer nacionalidad chilena***"
    else:
        mensaj_credito = "***Debe tener un salario mensual superior a $300000***"
else:
    mensaj_credito = "***Debe ser mayor de 24 años***"


if puede_sol_credito == True:
    print("--------------------------------------------------------")
    print(nombre , addr , rut)
    print("--------------------------------------------------------")
    print("Cumple con los requisitos")
    print(f" Sueldo: " , sueldo )
    print(f" Monto Máximo: " , m_max)
    print(f" Monto solicitado " , monto_s)
    print(f" Tasa mensual: 1,46% ")
    print(f"Cuotas: " , n_cuotas)
    print(f"Monto total a pagar: " , v_total )
    print("--------------------------------------------------------")
else:
    print("--------------------------------------------------------")
    print(nombre , addr , rut)
    print("--------------------------------------------------------")
    print("No cumple con los requisitos")
    print("--------------------------------------------------------")
    print(mensaj_credito)
    print("--------------------------------------------------------")
