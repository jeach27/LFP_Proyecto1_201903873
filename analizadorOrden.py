import Token
import Error
import funciones

Simbolos = []
Errores = []
fila = 0
columna = 0 
flagID = False
flagNumero = False
flagCadena = False
valor = ""
Atributos = []
estado = 0
flagAutomata = False

def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 160 and ord(c) <= 163) or ord(c) == 130

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
        Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'CADENA'))
        valor = ""
        flagCadena = False
        return 
    '''elif ord(c) == 32:# espacio
        longitud = len(valor)
        ultima = valor[longitud-1]
        if ultima == ' ':
            return
        else:
            columna += 1
            valor += c
            return'''
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
        longitud = len(valor)
        ultima = valor[longitud-1]
        if ultima == '.':
            Errores.append(Error.error(valor,'No se encontraron numeros, despues del punto decimal',fila,(columna-1-len(valor))))
        else:
            valor += c
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Porcentaje'))
            columna += 1
            valor = ""
            flagNumero = False
            return
    elif ord(c) == 44:#,
        longitud = len(valor)
        ultima = valor[longitud-1]
        if ultima == '.':
            Errores.append(Error.error(valor,'No se encontraron numeros, despues del punto decimal',fila,(columna-1-len(valor))))
        else:
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'NUMERO'))
        columna += 1
        valor = c
        Simbolos.append(Token.token(c,fila,(columna-2),'Simbolo_Coma'))
        valor = ''
        flagNumero = False
        return

    columna += 1
    longitud = len(valor)
    ultima = valor[longitud-1]
    if ultima == '.':
        Errores.append(Error.error(valor,'No se encontraron numeros, despues del punto decimal',fila,(columna-1-len(valor))))
    else:
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

def automata(s):
    global Atributos, estado, flagAutomata
    if estado == 1:
        if s.tipo == 'Simbolo_Coma':
            estado = 2
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_Coma',s.fila,s.columna))
    elif estado == 2:
        if s.tipo == 'CADENA':
            estado = 3
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaban Datos del cliente',s.fila,s.columna)) 
    elif estado == 3:
        if s.tipo == 'Simbolo_Coma':
            estado = 4
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_Coma',s.fila,s.columna))
    elif estado == 4:
        if s.tipo == 'CADENA':
            estado = 5
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaban Datos del cliente',s.fila,s.columna)) 
    elif estado == 5:
        if s.tipo == 'Simbolo_Coma':
            estado = 6
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_Coma',s.fila,s.columna))
    elif estado == 6:
        if s.tipo == 'Porcentaje':
            estado = 7
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba Porcentaje de propina',s.fila,s.columna))
    elif estado == 7:
        if s.tipo == 'NUMERO':
            estado = 8
            Atributos.append(s) 
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un numero',s.fila,s.columna))
    elif estado == 8:
        if s.tipo == 'Simbolo_Coma':
            estado = 9
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_Coma',s.fila,s.columna))
    elif estado == 9:
        if s.tipo == 'Identificador':
            estado = 7
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un identificador',s.fila,s.columna))

def ingreso(cadena):
    global estado,flagAutomata, Atributos
    caracteres=list(cadena)
    for c in caracteres:
        analizadorLexico(c)

    for s in Simbolos:
        if flagAutomata:
            automata(s)
        elif s.tipo == 'CADENA':
            estado = 1
            flagAutomata = True
            Atributos.append(Token.token(s.lexema, s.fila, s.columna ,s.tipo))
        else:
            Errores.append(Error.error(s,'Se esperaban Datos del cliente',s.fila,s.columna))


    if Errores:
        funciones.generarHTML_FER(Errores)
    elif Atributos:
        funciones.generarHTML_FS(Atributos)
    else:
        print('\nHa ocurrido un error ingrese el archivo nuevamente')
