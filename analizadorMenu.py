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
    global flagID, valor, fila, columna
    if isLetter(c) or isNumber(c):
        valor += c
        columna += 1
        return
    elif ord(c) == 95:#_
        valor += c
        columna += 1
        return
    elif ord(c) == 32:#"espacio
        #valor += c
        columna += 1
        if valor == 'restaurante' or valor == 'Restaurante':
            Simbolos.append(Token.token(valor,fila,(columna-1-len(valor)),'Palabra_Reservada'))
        else:
            Simbolos.append(Token.token(valor,fila,(columna-1-len(valor)),'Identificador'))
        valor = ""
        flagID = False
    elif ord(c) == 61:#=
        if valor == 'restaurante' or valor == 'Restaurante':
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Palabra_Reservada'))
        else:
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Identificador'))
        columna += 1
        Simbolos.append(Token.token('=',fila,(columna-2),'Simbolo_igual'))
        valor = ""
        flagID = False
    elif ord(c) == 59: #;
        if valor == 'restaurante' or valor == 'Restaurante':
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Palabra_Reservada'))
        else:
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'Identificador'))
        columna += 1
        Simbolos.append(Token.token(';',fila,(columna-2),'Simbolo_PuntoyComa'))
        valor = ""
        flagID = False
    else:
        Errores.append(Error.error(c,'identificador No valido',fila,columna))

def expresionNumero(c):
    global columna,fila,flagNumero,valor
    if isNumber(c):
        columna += 1
        valor += c
        return 
    elif ord(c) == 46:#.
        contadorP = 0
        for i in range(len(valor)):
            if valor[i] == '.':
                contadorP += 1
        if contadorP > 1:
            columna += 1
            valor += c
            Errores.append(Error.error(valor,'Se encontraron mas de 2 puntos decimal en un Numero',fila,(columna-1-len(valor))))
        else:
            columna += 1
            valor += c
            return
    elif ord(c) == 59:#;
        longitud = len(valor)
        ultima = valor[longitud-1]
        if ultima == '.':
            Errores.append(Error.error(valor,'No se encontraron numeros, despues del punto decimal',fila,(columna-1-len(valor))))
        else:
            Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'NUMERO'))
        columna += 1
        Simbolos.append(Token.token(';',fila,(columna-2),'Simbolo_PuntoyComa'))
        valor = ""
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

def expresionCadena(c):
    global flagCadena, fila, columna, valor
    if ord(c) == 39:#'
        columna += 1
        valor += c 
        Simbolos.append(Token.token(valor,fila,(columna-len(valor)),'CADENA'))
        valor = ""
        flagCadena = False
        return 
    #elif ord(c) == 10: #salto de linea

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
    
def analizadorLexico(c):
    global flagID, flagCadena, flagNumero, fila, columna, valor
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
        flagNumero =True
        valor = c
    elif ord(c) == 59: #;
        columna += 1
        valor = c
        Simbolos.append(Token.token(';',fila,(columna-2),'Simbolo_PuntoyComa'))
        valor = ""
    elif ord(c) == 39: #'
        flagCadena = True 
        valor = c
        columna += 1
    elif ord(c) == 91: #[
        columna += 1
        valor = c
        Simbolos.append(Token.token('[',fila,(columna-2),'Simbolo_Llave_Abierta'))
        valor = ""
    elif ord(c) == 93: #]
        columna += 1
        valor = c
        Simbolos.append(Token.token(']',fila,(columna-2),'Simbolo_Llave_Cerrada'))
        valor = ""
    elif ord(c) == 44: #,
        columna += 1
        valor = c
        Simbolos.append(Token.token(',',fila,(columna-2),'Simbolo_Coma'))
        valor = ""
    elif ord(c) == 61:#=
        columna += 1
        valor = c
        Simbolos.append(Token.token('=',fila,(columna-2),'Simbolo_igual'))
        valor = ""
    elif ord(c) == 10: #salto de linea
        fila += 1
        columna = 0
        valor = ""
    elif ord(c) == 32: #espacio
        valor = ""
    elif ord(c) == 58:# :
        columna += 1
        valor = c
        Simbolos.append(Token.token(':',fila,(columna-2),'Simbolo_Dos_Puntos'))
        Simbolos[-2].tipo = 'NombreSeccion'
        valor = ""
    else: 
        Errores.append(Error.error(c,'Caracter desconocido',fila,columna))

def automata(s):
    global Atributos, estado, flagAutomata
    if estado == 1:
        if s.tipo == 'Simbolo_igual':
            estado = 2
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba Simbolo_igual',s.fila,s.columna))
    elif estado == 2:
        if s.tipo == 'CADENA':
            estado = 3
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba una cadena como nombre del restaurante', s.fila, s.columna))
    elif estado == 3:
        if s.tipo == 'NombreSeccion':
            estado = 4
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba el nombre de una seccion',s.fila,s.columna))
    elif estado == 4:
        if s.tipo == 'Simbolo_Dos_Puntos':
            estado = 5
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema, 'Se esperaba un Simbolo_Dos_Puntos', s.fila,s.columna))
    elif estado == 5:
        if s.tipo == 'Simbolo_Llave_Abierta':
            estado = 6
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_Llave_Abierta', s.fila ,s.columna))
    elif estado == 6:
        if s.tipo == 'Identificador':
            estado = 7
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Identificador', s.fila,s.columna))
    elif estado == 7:
        if s.tipo == 'Simbolo_PuntoyComa':
            estado = 8
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_PuntoyComa',s.fila ,s.columna))
    elif estado == 8:
        if s.tipo == 'CADENA':
            estado = 9
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba una Cadena',s.fila,s.columna))
    elif estado == 9:
        if s.tipo == 'Simbolo_PuntoyComa':
            estado = 10
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_PuntoyComa',s.fila ,s.columna))
    elif estado == 10:
        if s.tipo == 'NUMERO':
            estado = 11
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Numero',s.fila,s.columna))
    elif estado == 11:
        if s.tipo == 'Simbolo_PuntoyComa':
            estado = 12
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_PuntoyComa',s.fila ,s.columna))
    elif estado == 12:
        if s.tipo == 'CADENA':
            estado = 13
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba una Cadena',s.fila,s.columna))
    elif estado == 13:
        if s.tipo == 'Simbolo_Llave_Cerrada':
            estado = 14
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba un Simbolo_Llave_Cerrada',s.fila,s.columna))
    elif estado == 14:
        if s.tipo == 'Simbolo_Llave_Abierta':
            estado = 6
        elif s.tipo == 'NombreSeccion':
            estado = 4
            Atributos.append(s)
        else:
            estado = -1
            flagAutomata = False
            Errores.append(Error.error(s.lexema,'Se esperaba otro tipo de token',s.fila,s.columna))
 
def ingreso(cadena, Limite):
    global estado, Atributos, flagAutomata,fila,columna,flagID,flagNumero,flagCadena,valor
    fila = 0
    columna = 0 
    flagID = False
    flagNumero = False
    flagCadena = False
    valor = ""
    estado = 0
    flagAutomata = False
    Simbolos.clear()
    Atributos.clear()
    Errores.clear()
    caracteres=list(cadena)
    for c in caracteres:
        analizadorLexico(c)

    for s in Simbolos:
        #print(s.lexema+ s.tipo)
        if flagAutomata:
            automata(s)
        elif s.tipo == 'Palabra_Reservada':
            estado = 1
            flagAutomata = True
            Atributos.append(s)
        else:
            Errores.append(Error.error(s.lexema,'Se esperaba una Palabra Reservada',s.fila,s.columna))

    if Errores:
        funciones.generarHTML_MER(Errores)
        return -1,Errores
    elif Atributos:
        funciones.generarHTML_MS(Atributos,Limite)
        return 1,Atributos
    else:
        print('\n-> Ha ocurrido un error ingrese el archivo nuevamente')

    

