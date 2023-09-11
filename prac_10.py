'''hacer un programa que llene obligatoriamente un arreglo de numeros de 5 pisiciones
previamente validados, y al finalizar debe mostrar cuantos pares y cuantos impares 
hay en el arreglo'''

def validarnumeros(numeros):
    if numeros.isdigit():
        return int(numeros)
    else:
        print('no es numero')
        return 0

num = [0,0,0,0,0]
pos = 0
valida = 0
cp = 0
cim = 0
for i in range (5):
    b = input('escribe un numero')
    valida = validarnumeros(b)
    if not valida == 0:
        num[i] = b
        num[pos] = valida
        pos +=1

for i in num:
    if i %2 == 0:
        cp += 1
    else:
        cim += 1

print('numero de pares: ', cp, 'numero de impares: ',cim)

