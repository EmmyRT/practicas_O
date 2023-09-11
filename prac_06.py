conv = 'si'
while conv == 'si':
    def leerDatos():
        a = input('escribe un valor')
        return a 
    def validarDatos(a):
        if a.isdigit():
            return 'son numeros'
        else:
            return ' no es numero '
    b = leerDatos()
    print(validarDatos(b))
    conv = input('quieres volver a intentar?')