# arreglos
def validarnumeros(numeros):
    if numeros.isdigit():
        return int(numeros)
    else:
        print('no es numero')
        return 0
    
b = ""
a = [0,0,0,0,0,0,0,0,0,0]
pos = 0
v = 0
while(b==""):
    b = input('escribe un valor:')
    v = validarnumeros(b)
    if not v == 0:
        a[pos] = v
        pos += 1
        res = input('deseas otro')
        if res == 's':
            if pos >= 9:
                print('arreglo lleno')
                break
            b = ""
    else:
        b =""
for i in a:
    if not i == 0:
        print(i, "\n")        

