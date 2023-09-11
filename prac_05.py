'''hacer un programa que lea el nombre y el precio de un producto
el programa repitira esta accion haste que el usuario lo desee
y al finalizar mostrara el total de poductos, la sumatoria de 
los precios el porcentaje del iva y el total a pagar'''
res = 'si'
s = 0
n = 0
ivt = 0
while res == 'si':
    print('Hola! bienvenido!! \n')
    pro = input('Ingrese el nombre del producto \n')
    pre = float(input('Ingrese el precio del producto \n'))
    s += pre
    n += 1
    ivt = s * 0.16
    tot = ivt + s
    res = input('Desea agregar otro roducto (si)-(no): \n')
print('Cantidad de productos ingresados: ',n)
print('Total: ' ,s)
print('iva: ',ivt)
print('Total a pagar: ',tot)
