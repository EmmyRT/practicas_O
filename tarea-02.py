'''
hacer un program que mueste el siguiente menu
1- suma
2- resta
3- multiplicacion
4- divicion con entero
5- divicion con decimal
6- potencia
7- raiz
'''
# import math as mt
conv = 'si'
def menu():
    print('1-suma')
    print('2-resta')
    print('3-multiplicacion')
    print('4-divicion con entero')
    print('5-divicion con decimales')
    print('6-potencia')
    print('7-raiz')

def suma():
    a = int(input('escribe un numero \n'))
    b = int(input('escribe otro numero \n'))
    c = a + b
    print('el resultado es: ',c)
def resta():
    a = int(input('escribe un numero \n'))
    b = int(input('escribe otro numero \n'))
    c = a - b
    print('el resultado es: ',c)
def multiplicacion():
    a = int(input('escribe un numero \n'))
    b = int(input('escribe otro numero \n'))
    c = a * b
    print('el resultado es: ',c)
def divicionentero():
    a = int(input('escribe un numero \n'))
    b = int(input('escribe otro numero \n'))
    c = a // b
    print('el resultado es: ',c)
def diviciondecimal():
    a = float(input('escribe un numero \n'))
    b = float(input('escribe otro numero \n'))
    c = a / b
    print('el resultado es: ',c)
def potencia():
    a = int(input('escribe un numero \n'))
    c = a ** 2
    print('el resultado es: ',c)
def raiz():
    a = int(input('escribe un numero \n'))
    r = a ** (1/2)
    print('la raiz es: ',r)
    # aqui ciclo 
while conv == 'si':
    menu()   
    op = int(input('elige una opcion \n'))
    if op == 1:
        suma()
    if op == 2:
        resta()
    if op == 3:
        multiplicacion()
    if op == 4:
        divicionentero()
    if op == 5:
        diviciondecimal()
    if op == 6:
        potencia()
    if op == 7:
        raiz()
    elif op >7 or op <1:
        print('opcion incorrecta')
    conv = input('quiere otra operacion: si - no \n')
