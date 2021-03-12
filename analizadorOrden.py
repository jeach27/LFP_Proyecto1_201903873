import Token
import Error

Simbolos = []
Errores = []
fila = 0
columna = 0 
flagID = False
flagNumero = False
flagCadena = False
valor = ""

def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122)

def isNumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)

def expresionID(c):
    global flagID, fila, columna, valor
    if isLetter(c) or isNumber(c):
        valor += c
        columna += 1
        return
    elif ord(c) == 95:#_
        valor += c
        columna += 1
        return
    elif ord(c) == 32:#"espacio
        valor += c
        columna += 1
        Simbolos.append(Token.token(valor,fila,(columna-1-len(valor)),'Identificador'))
        valor = ""
        flagID = False
    elif ord(c) == 10:# salto de linea
        Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Identificador'))
        fila += 1
        columna = 0
        valor = ''
        flagID = False
    else:
        Errores.append(Error.error(c,'identificador No valido',fila,columna))

def expresionCadena(c):
    global flagCadena, fila, columna, valor
    if ord(c) == 39:#'
        columna += 1
        valor += c 
        Simbolos.append(Token.token(valor,fila,(columna-1-len(valor)),'CADENA'))
        valor = ""
        flagCadena = False
        return 
    elif ord(c) == 32:# espacio
        longitud = len(valor)
        ultima = valor[longitud-1]
        if ultima == ' ':
            return
        else:
            columna += 1
            valor += c
            return
    columna += 1
    valor += c

def expresionNumero(c): 
    global columna,fila,flagNumero,valor
    if isNumber(c):
        columna += 1
        valor += c
        return 
    elif ord(c) == 46:#.
        columna += 1
        valor += c
        return
    elif ord(c) == 37:#%
        valor += c
        Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Porcentaje'))
        columna += 1
        valor = ""
        flagNumero = False
        return
    elif ord(c) == 44:#,
        pass

    columna += 1
    Simbolos.append(Token.token(valor,fila,(columna-1-len(valor)),'NUMERO'))
    valor = ""
    flagNumero = False   

def analizadorLexico(c):
    global flagID, flagCadena, flagNumero, columna, fila, valor
    if flagID:
        expresionID(c)
    elif flagCadena:
        expresionCadena(c)
    elif flagNumero:
        expresionNumero(c)
    elif isLetter(c):
        columna += 1
        flagID = True
        valor = c
    elif isNumber(c):
        columna += 1
        flagNumero = True
        valor = c
    elif ord(c) == 39:#'
        flagCadena = True
        columna += 1
        valor = c
    elif ord(c) == 44:#,
        columna += 1
        valor = c
        Simbolos.append(Token.token(c,fila,(columna-2),'Simbolo_Coma'))
        valor = ''
    elif ord(c) == 10:# salto de linea
        fila += 1
        columna = 0
        valor = ''
    elif ord(c) == 32:#espacio
        valor = ''
    else:
        Errores.append(Error.error(c,'Caracter desconocido',fila,columna))

def ingreso(cadena):
    caracteres=list(cadena)
    for c in caracteres:
        analizadorLexico(c)
        
    for s in Simbolos:
        print(s.lexema+s.tipo)

    for a in Errores:
        print(a.lexema+ a.descripcion)