def validar_nombre(nombre):
    resp = False
    mensaje = 'Usted ha introdicido caracteres no validos'
    if(nombre == 'a'):
        resp = True
        print('Usted a usado el usuario a, y este es incorrecto use otro usuario.')
    return resp

def crear_id(nombre):
    id = 0
    return id

def main():
    validacion = True
    nombre = ''
    while(validacion):
        nombre = input('Introduzca el nuevo nombre de usuario: ')
        validacion = validar_nombre(nombre)
    id = crear_id(nombre)
    print(id)

if __name__ == '__main__':
    main()
