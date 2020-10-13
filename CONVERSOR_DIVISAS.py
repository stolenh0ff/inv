import os
os.system("cls")


#Valores monedas en clp
valor_dolar = 801.6
valor_euro = 875.4
valor_uf = 28993.7
valor_clp = 1

#Var
sep = ("------------------------------------------------------")

#Operaciones
#Operacion_1 --->>>Selecciona la moneda de origen
#Operacion_2 --->>>Selecciona método de conversión

print("Banco Oeste")
print("1) Dólares")
print("2) Euro")
print("3) UF")
print("4) Salir")

operacion_1 = int(input("Seleccione la moneda a operar: "))

if operacion_1 == 1:
    print(sep)
    print("Seleccione método de conversión")
    print("1) Peso Chileno a Dolar (CLP a USD)")
    print("2) Dolar a Peso Chileno (USD a CLP)")
    moneda_A = "Pesos Chilenos"
    moneda_B = "Dolares"

if operacion_1 == 2:
    print(sep)
    print("Seleccione método de conversión")
    print("1) Peso Chileno a Euro (CLP a EUR)")
    print("2) Euro a Peso Chileno (EUR a CLP)")
    moneda_A = "Pesos Chilenos"
    moneda_B = "Euros"

if operacion_1 == 3:
    print(sep)
    print("Seleccione método de conversión")
    print("1) Peso Chileno a Unidad de Fomento (CLP a UF)")
    print("2) Unidad de Fomento a Peso Chileno (UF a CLP)")
    moneda_A = "Pesos Chilenos"
    moneda_B = "Unidades de Fomento"

if operacion_1 == 4:
    exit

operacion_2 = int(input("--->>> "))


if operacion_2 == 1:
    print("Ingresa cantidad de", moneda_A )
    cant_mon_A = float(input("--->>> "))
if operacion_2 == 2:
    print("Ingresa cantidad de", moneda_B )
    cant_mon_B = float(input("--->>> "))

#OPERACION MATEMÁTICA

#Conversion directa




#Conversion inversa





