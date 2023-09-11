'''hacer un programa con 3 numeros validados y
 que muestre el mayor, el menor y el de medias'''
def dato1():
    a = input('escribe un numero \n')
    return a
def dato2():
    b = input('escribe un numero \n')
    return b
def dato3():
    c = input('escribe un numero \n')
    return c

def validarDatos(a, b ,c):
    if(a.isdigit() and b.isdigit() and c.isdigit()):
        q = int(a)
        w = int(b)
        e = int(c)
        print('son numerons')
        if q > w:
            if q > e:
                print('el mayor es:',q)
                if w > e:
                    print('es menor:', w)
                    print('medio:',e)
            elif q < e:
                print('el mayor es:',e)
    else:
        print('no son numeros')
    
d1 = dato1()
d2 = dato2()
d3 = dato3()
print(validarDatos(d1, d2, d3))
