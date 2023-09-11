'''TAREA: hacer un programa que mueste en pantalla un menu 
1- area de un cuadrado.
2- area de un circulo.
3- area de triagulo.
dependiendo de la opcion del menu se pedira los datos correspondientes
para calcular el area.
'''
a = 1
acu = 0
at = 0
aci = 0
while a == 1:
    print('"BIENVENIDO!!"')
    print('¿QUE AREA QUIERES CALCULAR?')
    print('1. CUADRADO')
    print('2. CIRCULO')
    print('3. TRIANGULO')
    nu = int(input('INGRESE EL NUMERO DE LA FIGURA \n'))
    if nu == 1:
        cu = int(input('Agrege la medidad de un lado del cuadrado \n'))
        acu = cu * cu
        print('El area del cuadrado es: ',acu)
    if nu == 2:
        ci = int(input('Agrege el radio del circulo \n'))
        aci = (ci ** 2) * 3.14
        print('El area del circulo es: ',aci)
    if nu == 3:
        ba = int(input('Agrege la base del trinagulo \n'))
        al = int(input('Agrege la altura del triangulo \n'))
        at = (ba * al)/2
        print('El area del trinagulo es: ',at)
    a = int(input('¿Quiere calcular alguna otra area?, 1 = SI, 2 = NO \n'))
    
