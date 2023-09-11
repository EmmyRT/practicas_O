'''hacer un programa que lea nombre, precio y cantidad de un producto
datos prebiamente validados, donde el usuario determinara cuantos productos
se van a introducir y al finalizar mostrara el total sin iva, el iva total de 
productos y el total a pagar'''
def validarnumeros(numeros):
    if numeros.isdigit():
        return True
    else:
        return False
def validarletras(nombre):
    if nombre.isdigit():
        return False
    else:
        return True
def pedirdatos():
    global total
    global nombre
    nombre = ""
    global numeros
    numeros = ""
    global precio
    precio = 0
    global cantidad
    cantidad = 0
    while (True):
        nombre = input('escribe un produto \n')
        res = validarletras(nombre)
        if res == True:
            break
        else:
            print('error no es un nombre de producto')
    while(True):
        numeros = input('escribe un precio \n')
        res = validarnumeros(numeros)
        if res == True:
            precio = int(numeros)
            break
        else:
            print('no es precio de producto')
    while(True):
        numeros = input('escribe una cantidad de productos \n')
        res = validarnumeros(numeros)
        if res == True:
            cantidad = int(numeros)
            total += cantidad * precio
            break
        else:
            print('no es una cantidad')
global numeros
global nombre
global precio
global cantidad
global total
total = 0
while(True):
    pedirdatos()
    r = input('deseas otro prpducto \n')
    if not r == 'si':
        print('el total: ', total)
        iva = total * 0.16
        print('iva total: ', iva)
        tp = total + iva
        print('total a pagar es: ', tp)
        break
# print('El producto es: {0}\nCon precio de: {1}\nCantidad de: {2} productos'.format(nombre,precio,cantidad))
