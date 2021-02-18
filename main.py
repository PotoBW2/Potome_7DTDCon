from random import randint

def validar_nombre(nombre):
    resp = False
    if(len(nombre) < 4):
        print('El nombre debe tener almenos 4 caracteres')
        resp = True
    if (len(nombre) > 16):
        print('El nombre no puede tener más de 16 caracteres')
        resp = True

    mensaje = 'ERROR ERROR ERROR ERROR\nUsted ha introdicido caracteres no validos:'
    count_error = 1

    if (nombre.count('`') > 0):
        mensaje += '\n%s- Ha usado el caracter `' % count_error
        count_error += 1

    if (nombre.count('~') > 0):
        mensaje += '\n%s- Ha usado el caracter ~' % count_error
        count_error += 1

    if (nombre.count('!') > 0):
        mensaje += '\n%s- Ha usado el caracter !' % count_error
        count_error += 1

    if (nombre.count('@') > 0):
        mensaje += '\n%s- Ha usado el caracter @' % count_error
        count_error += 1

    if (nombre.count('#') > 0):
        mensaje += '\n%s- Ha usado el caracter #' % count_error
        count_error += 1

    if (nombre.count('$') > 0):
        mensaje += '\n%s- Ha usado el caracter $' % count_error
        count_error += 1

    if (nombre.count('%') > 0):
        mensaje += '\n%s- Ha usado el caracter ' % count_error
        mensaje += '%'
        count_error += 1

    if (nombre.count('^') > 0):
        mensaje += '\n%s- Ha usado el caracter ^' % count_error
        count_error += 1

    if (nombre.count('&') > 0):
        mensaje += '\n%s- Ha usado el caracter &' % count_error
        count_error += 1

    if (nombre.count('*') > 0):
        mensaje += '\n%s- Ha usado el caracter *' % count_error
        count_error += 1

    if (nombre.count('(') > 0):
        mensaje += '\n%s- Ha usado el caracter (' % count_error
        count_error += 1

    if (nombre.count(')') > 0):
        mensaje += '\n%s- Ha usado el caracter )' % count_error
        count_error += 1

    if (nombre.count('-') > 0):
        mensaje += '\n%s- Ha usado el caracter - ' % count_error
        count_error += 1

    if (nombre.count('_') > 0):
        mensaje += '\n%s- Ha usado el caracter _ ' % count_error
        count_error += 1

    if (nombre.count('=') > 0):
        mensaje += '\n%s- Ha usado el caracter =' % count_error
        count_error += 1

    if (nombre.count('+') > 0):
        mensaje += '\n%s- Ha usado el caracter +' % count_error
        count_error += 1

    if (nombre.count('\\') > 0):
        mensaje += '\n%s- Ha usado el caracter \\' % count_error
        count_error += 1

    if (nombre.count('|') > 0):
        mensaje += '\n%s- Ha usado el caracter |' % count_error
        count_error += 1

    if (nombre.count('[') > 0):
        mensaje += '\n%s- Ha usado el caracter [' % count_error
        count_error += 1

    if (nombre.count(']') > 0):
        mensaje += '\n%s- Ha usado el caracter ]' % count_error
        count_error += 1

    if (nombre.count('{') > 0):
        mensaje += '\n%s- Ha usado el caracter {' % count_error
        count_error += 1

    if (nombre.count('}') > 0):
        mensaje += '\n%s- Ha usado el caracter }' % count_error
        count_error += 1

    if (nombre.count(';') > 0):
        mensaje += '\n%s- Ha usado el caracter ;' % count_error
        count_error += 1

    if (nombre.count(':') > 0):
        mensaje += '\n%s- Ha usado el caracter :' % count_error
        count_error += 1

    if (nombre.count('"') > 0):
        mensaje += '\n%s- Ha usado el caracter "' % count_error
        count_error += 1

    if (nombre.count("'") > 0):
        mensaje += "\n%s- Ha usado el caracter '" % count_error
        count_error += 1

    if (nombre.count(',') > 0):
        mensaje += '\n%s- Ha usado el caracter ,' % count_error
        count_error += 1

    if (nombre.count('<') > 0):
        mensaje += '\n%s- Ha usado el caracter <' % count_error
        count_error += 1

    if (nombre.count('>') > 0):
        mensaje += '\n%s- Ha usado el caracter >' % count_error
        count_error += 1

    if (nombre.count('.') > 0):
        mensaje += '\n%s- Ha usado el caracter .' % count_error
        count_error += 1

    if (nombre.count('?') > 0):
        mensaje += '\n%s- Ha usado el caracter ?' % count_error
        count_error += 1

    if (nombre.count('/') > 0):
        mensaje += '\n%s- Ha usado el caracter /' % count_error
        count_error += 1

    if (nombre.count('è') > 0):
        mensaje += '\n%s- Ha usado el caracter è' % count_error
        count_error += 1

    if (nombre.count('ù') > 0):
        mensaje += '\n%s- Ha usado el caracter ù' % count_error
        count_error += 1

    if (nombre.count('ì') > 0):
        mensaje += '\n%s- Ha usado el caracter ì' % count_error
        count_error += 1

    if (nombre.count('ò') > 0):
        mensaje += '\n%s- Ha usado el caracter ò' % count_error
        count_error += 1

    if (nombre.count('à') > 0):
        mensaje += '\n%s- Ha usado el caracter à' % count_error
        count_error += 1

    if (nombre.count('õ') > 0):
        mensaje += '\n%s- Ha usado el caracter õ' % count_error
        count_error += 1

    if (nombre.count('ã') > 0):
        mensaje += '\n%s- Ha usado el caracter ã' % count_error
        count_error += 1

    if (nombre.count('ñ') > 0):
        mensaje += '\n%s- Ha usado el caracter ñ' % count_error
        count_error += 1

    if (nombre.count('È') > 0):
        mensaje += '\n%s- Ha usado el caracter È' % count_error
        count_error += 1

    if (nombre.count('Ù') > 0):
        mensaje += '\n%s- Ha usado el caracter Ù' % count_error
        count_error += 1

    if (nombre.count('Ì') > 0):
        mensaje += '\n%s- Ha usado el caracter Ì' % count_error
        count_error += 1

    if (nombre.count('Ò') > 0):
        mensaje += '\n%s- Ha usado el caracter Ò' % count_error
        count_error += 1

    if (nombre.count('À') > 0):
        mensaje += '\n%s- Ha usado el caracter À' % count_error
        count_error += 1

    if (nombre.count('Õ') > 0):
        mensaje += '\n%s- Ha usado el caracter Õ' % count_error
        count_error += 1

    if (nombre.count('Ã') > 0):
        mensaje += '\n%s- Ha usado el caracter Ã' % count_error
        count_error += 1

    if (nombre.count('Ñ') > 0):
        mensaje += '\n%s- Ha usado el caracter Ñ' % count_error
        count_error += 1

    if (nombre.count('ê') > 0):
        mensaje += '\n%s- Ha usado el caracter ê' % count_error
        count_error += 1

    if (nombre.count('û') > 0):
        mensaje += '\n%s- Ha usado el caracter û' % count_error
        count_error += 1

    if (nombre.count('î') > 0):
        mensaje += '\n%s- Ha usado el caracter î' % count_error
        count_error += 1

    if (nombre.count('ô') > 0):
        mensaje += '\n%s- Ha usado el caracter ô' % count_error
        count_error += 1

    if (nombre.count('â') > 0):
        mensaje += '\n%s- Ha usado el caracter â' % count_error
        count_error += 1

    if (nombre.count('Ê') > 0):
        mensaje += '\n%s- Ha usado el caracter Ê' % count_error
        count_error += 1

    if (nombre.count('Û') > 0):
        mensaje += '\n%s- Ha usado el caracter Û' % count_error
        count_error += 1

    if (nombre.count('Î') > 0):
        mensaje += '\n%s- Ha usado el caracter Î' % count_error
        count_error += 1

    if (nombre.count('Ô') > 0):
        mensaje += '\n%s- Ha usado el caracter Ô' % count_error
        count_error += 1

    if (nombre.count('Â') > 0):
        mensaje += '\n%s- Ha usado el caracter Â' % count_error
        count_error += 1

    if (nombre.count('ç') > 0):
        mensaje += '\n%s- Ha usado el caracter ç' % count_error
        count_error += 1

    if (nombre.count('é') > 0):
        mensaje += '\n%s- Ha usado el caracter é' % count_error
        count_error += 1

    if (nombre.count('ý') > 0):
        mensaje += '\n%s- Ha usado el caracter ý' % count_error
        count_error += 1

    if (nombre.count('ú') > 0):
        mensaje += '\n%s- Ha usado el caracter ú' % count_error
        count_error += 1

    if (nombre.count('í') > 0):
        mensaje += '\n%s- Ha usado el caracter í' % count_error
        count_error += 1

    if (nombre.count('ó') > 0):
        mensaje += '\n%s- Ha usado el caracter ó' % count_error
        count_error += 1

    if (nombre.count('á') > 0):
        mensaje += '\n%s- Ha usado el caracter á' % count_error
        count_error += 1

    if (nombre.count('É') > 0):
        mensaje += '\n%s- Ha usado el caracter É' % count_error
        count_error += 1

    if (nombre.count('Ý') > 0):
        mensaje += '\n%s- Ha usado el caracter Ý' % count_error
        count_error += 1

    if (nombre.count('Ú') > 0):
        mensaje += '\n%s- Ha usado el caracter Ú' % count_error
        count_error += 1

    if (nombre.count('Í') > 0):
        mensaje += '\n%s- Ha usado el caracter Í' % count_error
        count_error += 1

    if (nombre.count('Ó') > 0):
        mensaje += '\n%s- Ha usado el caracter Ó' % count_error
        count_error += 1

    if (nombre.count('Á') > 0):
        mensaje += '\n%s- Ha usado el caracter Á' % count_error
        count_error += 1

    if (nombre.count('Ç') > 0):
        mensaje += '\n%s- Ha usado el caracter Ç' % count_error
        count_error += 1

    if (nombre.count('ë') > 0):
        mensaje += '\n%s- Ha usado el caracter ë' % count_error
        count_error += 1

    if (nombre.count('ÿ') > 0):
        mensaje += '\n%s- Ha usado el caracter ÿ' % count_error
        count_error += 1

    if (nombre.count('ü') > 0):
        mensaje += '\n%s- Ha usado el caracter ü' % count_error
        count_error += 1

    if (nombre.count('ï') > 0):
        mensaje += '\n%s- Ha usado el caracter ï' % count_error
        count_error += 1

    if (nombre.count('ö') > 0):
        mensaje += '\n%s- Ha usado el caracter ö' % count_error
        count_error += 1

    if (nombre.count('ä') > 0):
        mensaje += '\n%s- Ha usado el caracter ä' % count_error
        count_error += 1

    if (nombre.count('Ë') > 0):
        mensaje += '\n%s- Ha usado el caracter Ë' % count_error
        count_error += 1

    if (nombre.count('Ü') > 0):
        mensaje += '\n%s- Ha usado el caracter Ü' % count_error
        count_error += 1

    if (nombre.count('Ï') > 0):
        mensaje += '\n%s- Ha usado el caracter Ï' % count_error
        count_error += 1

    if (nombre.count('Ö') > 0):
        mensaje += '\n%s- Ha usado el caracter Ö' % count_error
        count_error += 1

    if (nombre.count('Ä') > 0):
        mensaje += '\n%s- Ha usado el caracter Ä ' % count_error
        count_error += 1

    if (nombre.count('π') > 0):
        mensaje += '\n%s- Ha usado el caracter π ' % count_error
        count_error += 1

    if (nombre.count(' ') > 0):
        mensaje += '\n%s- No se permite usar espacios ' % count_error
        count_error += 1

    if (not (nombre.isalnum())):
        count_error += 1

    if (count_error > 1):
        mensaje += '\nDebe introdicir nuevamente en nombre del usuario'
        print(mensaje)
        resp = True
    return resp


def crear_id(nombre):
    id = 0
    tamanno = True
    for letra in nombre:
        if (letra == 'a'):
            id += 1
        if (letra == 'b'):
            id += 2
        if (letra == 'c'):
            id += 3
        if (letra == 'd'):
            id += 4
        if (letra == 'f'):
            id += 5
        if (letra == 'g'):
            id += 6
        if (letra == 'h'):
            id += 7
        if (letra == 'i'):
            id += 8
        if (letra == 'j'):
            id += 9
        if (letra == 'k'):
            id += 10
        if (letra == 'l'):
            id += 11
        if (letra == 'm'):
            id += 12
        if (letra == 'n'):
            id += 13
        if (letra == 'o'):
            id += 14
        if (letra == 'p'):
            id += 15
        if (letra == 'q'):
            id += 16
        if (letra == 'r'):
            id += 17
        if (letra == 's'):
            id += 18
        if (letra == 't'):
            id += 19
        if (letra == 'u'):
            id += 20
        if (letra == 'v'):
            id += 21
        if (letra == 'w'):
            id += 22
        if (letra == 'x'):
            id += 23
        if (letra == 'y'):
            id += 24
        if (letra == 'z'):
            id += 25
        if (letra == 'A'):
            id += 26
        if (letra == 'B'):
            id += 27
        if (letra == 'C'):
            id += 28
        if (letra == 'D'):
            id += 29
        if (letra == 'F'):
            id += 30
        if (letra == 'G'):
            id += 31
        if (letra == 'H'):
            id += 32
        if (letra == 'I'):
            id += 33
        if (letra == 'J'):
            id += 34
        if (letra == 'K'):
            id += 35
        if (letra == 'L'):
            id += 36
        if (letra == 'M'):
            id += 37
        if (letra == 'N'):
            id += 38
        if (letra == 'O'):
            id += 39
        if (letra == 'P'):
            id += 40
        if (letra == 'Q'):
            id += 41
        if (letra == 'R'):
            id += 42
        if (letra == 'S'):
            id += 43
        if (letra == 'T'):
            id += 44
        if (letra == 'U'):
            id += 45
        if (letra == 'V'):
            id += 46
        if (letra == 'W'):
            id += 47
        if (letra == 'X'):
            id += 48
        if (letra == 'Y'):
            id += 49
        if (letra == 'Z'):
            id += 50
        if (letra == '1'):
            id += 51
        if (letra == '2'):
            id += 52
        if (letra == '3'):
            id += 53
        if (letra == '4'):
            id += 54
        if (letra == '5'):
            id += 55
        if (letra == '6'):
            id += 56
        if (letra == '7'):
            id += 57
        if (letra == '8'):
            id += 58
        if (letra == '9'):
            id += 59
        if (letra == '0'):
            id += 60
        if (letra == '_'):
            id += 61
        id *= 10
    while(tamanno):
        if(id < 99999999999999999):
            id *= randint(1,10)
        else:
            tamanno = False
    id = str(id)
    id = id[0:17]
    return id


def main():
    validacion = True
    nombre = ''
    while (validacion):
        nombre = input('Introduzca el nuevo nombre de usuario: ')
        validacion = validar_nombre(nombre)
    id = crear_id(nombre)
    print(id)


if __name__ == '__main__':
    main()
