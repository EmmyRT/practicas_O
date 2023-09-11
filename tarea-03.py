'''hacer un programa que en un areglo de string de 7 posiciones se pida, se valide, se pase el
arreglo los dias de la semana sin repetir y al final se muestre'''
def validarletras(letras):
    if letras.isalpha():
        return (letras)
    else:
        print('\nSolo se permiten letras!!\n')
        return 0
    
validar = 0    
dias = []
registros = set()
for i in range (7):
    dias = input('\nIngrese un día de la semana \n')
    validar = validarletras(dias)
    if dias in registros:
        print('Los siento, pero este día ya esta registrado')
    else:
        registros.add(dias)

print('\nLos días de la semana registrados son: \n')
for dias in registros:
    print(dias)
    
print('\nADIOS!')