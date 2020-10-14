import os
os.system("cls")

#Var
sep = ("------------------------------------------------------")
intentos = 0

#Valor Dolar
valor_usd = 801.6
#Valor Euro
valor_eur = 875.4
#Valor Unidad de Fomento
valor_clf = 28993.7

#Operaciones
#Operacion_1 --->>>Selecciona la moneda de origen [MENU PRINCIPAL]
#Operacion_2 --->>>Selecciona método de conversión

print("Banco Oeste")
print("1) Dólares")
print("2) Euro")
print("3) UF")
print("4) Salir")

#(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)
#(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)
#(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)

operacion_1 = 0
while (operacion_1 < 1 or operacion_1 > 4) and intentos < 3:
    intentos = intentos + 1
    operacion_1 = int(input("Seleccione la moneda a operar: "))
if intentos == 3:
    print(sep)
    print("Ha alcanzado el limite máximo de intentos (3 intentos)")
    print(sep)
    exit()

#(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)
#(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)
#(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)(TESTING)

if operacion_1 == 1:
    print(sep)
    print("Seleccione método de conversión")
    print("1) Peso Chileno a Dólar (CLP a USD)")
    print("2) Dolar a Peso Chileno (USD a CLP)")
    moneda_A = "Pesos Chilenos"
    moneda_B = "Dólares"
    operacion_2 = int(input("--->>> "))

if operacion_1 == 2:
    print(sep)
    print("Seleccione método de conversión")
    print("1) Peso Chileno a Euro (CLP a EUR)")
    print("2) Euro a Peso Chileno (EUR a CLP)")
    moneda_A = "Pesos Chilenos"
    moneda_B = "Euros"
    operacion_2 = int(input("--->>> "))

if operacion_1 == 3:
    print(sep)
    print("Seleccione método de conversión")
    print("1) Peso Chileno a Unidad de Fomento (CLP a CLF)")
    print("2) Unidad de Fomento a Peso Chileno (CLF a CLP)")
    moneda_A = "Pesos Chilenos"
    moneda_B = "Unidades de Fomento"
    operacion_2 = int(input("--->>> "))

if operacion_1 == 4:
    print("Presione [ENTER] para confirmar")
    input()
    exit()

if operacion_2 == 1:
    print("Ingresa cantidad de", moneda_A )
    cant_mon_A = float(input("--->>> "))
    if operacion_1 ==1: 
        valor_m = valor_usd
        iso_code = "USD"
    if operacion_1 ==2:
        valor_m = valor_eur
        iso_code = "EUR"
    if operacion_1 ==3:
        valor_m = valor_clf
        iso_code = "CLF"
    #Conversion directa (A -->> B)
    v_total = cant_mon_A / valor_m
elif operacion_2 == 2:
    print("Ingresa cantidad de", moneda_B )
    cant_mon_B = float(input("--->>> "))
    if operacion_1 ==1: 
        valor_m = valor_usd
    if operacion_1 ==2:
        valor_m = valor_eur
    if operacion_1 ==3:
        valor_m = valor_clf
    iso_code = "CLP"
    #Conversion inversa (B -->> A)
    v_total = cant_mon_B * valor_m

print("Valor Total: ", v_total, iso_code )
#BS
