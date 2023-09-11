# estructuras repetitivas
'''a = 'hola'
for i in range(1,10):
    print(i)#serie
for i in a:
     print(i) #recorrer string
for i in [7,10]:
    print(i) #datos espesificos

Hacer un programa que lea 5 numeros y mustre cuantos
pares y impares hay

p = 0
y = 0
for i in range(0,5):
    a = int(input('escribe un numero \n'))
    if a % 2 == 0:
        p += 1
    else:
        y += 1
print('pares = ',p,'impares = ',y)
'''
a = 0
p=0
y=0
while(a<5):
    v = int(input('escribe un numero \n'))
    if a % 2 == 0:
        p += 1
    else:
        y += 1
    a += 1
print('pares = ',p,'impares = ',y)
