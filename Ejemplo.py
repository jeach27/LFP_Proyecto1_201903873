class Simbolo:

    def __init__(self,token,lexema,linea,columna):
        self.token = token 
        self.lexema = lexema 
        self.linea = linea
        self.columna = columna 

class Atributo:
    def __init__(self,id,valor):
        self.id = id
        self.valor = valor

tablaSimbolos = []
tablaAtributos = []
fila = 0
columna = 0
flagExpresionId = False
flagExpresionCadena = False
flagExpresionNumero = False
valor = ""
estado = 0
temp = None
flagAutomataObjeto = False

def mostrarError(simbolo,expectativa,linea,columna):
    print("Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " + expectativa + " linea: " + str(linea) + ", columna: " + str(columna) )

def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122)

def isNumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)

def expresionRegularId(c):
    global valor,columna,fila,flagExpresionId
    
    if isLetter(c) or isNumber(c):
        valor += c
        columna += 1
        return
    elif ord(c) == 32:
        valor += c
        columna += 1
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna - 1 - len(valor))))
        valor = ""
        flagExpresionId = False
    elif ord(c) == 61:
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna  - len(valor))))
        columna += 1
        tablaSimbolos.append(Simbolo("simbolo_igual","=",fila,(columna - 2)))
        valor = ""
        flagExpresionId = False
    else:
        mostrarError(c,"",fila,columna)

def expresionRegularCadena(c):
    global valor,columna,fila,flagExpresionCadena 

    if ord(c) == 34:
        columna += 1
        valor += c 
        tablaSimbolos.append(Simbolo("CADENA",valor,fila,(columna - 1 - len(valor))))
        valor = ""
        flagExpresionCadena = False
        return 
    
    columna += 1
    valor += c

def expresionRegularNumero(c):
    global columna,fila,flagExpresionNumero,valor
    if isNumber(c):
        columna += 1
        valor += c
        return 

    columna += 1
    tablaSimbolos.append(Simbolo("NUMERO",valor,fila,(columna - 1 - len(valor))))
    valor = ""
    flagExpresionNumero = False

def analizadorLexico(c):
    global fila,columna,flagExpresionId,valor,flagExpresionCadena,flagExpresionNumero,valor
    if flagExpresionId:
        expresionRegularId(c)
    elif flagExpresionCadena:
        expresionRegularCadena(c)
    elif flagExpresionNumero:
        expresionRegularNumero(c)
    elif isLetter(c):
        columna += 1
        flagExpresionId = True
        valor = c
    elif isNumber(c):
        columna += 1 
        valor = c
        flagExpresionNumero = True
    elif ord(c) == 61: #=
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_igual","=",fila,(columna - 2)))
        valor = ""
    elif ord(c) == 34: #""
        flagExpresionCadena = True 
        valor = c
        columna += 1
    elif ord(c) == 91: #[
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_llave_abre",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 93: #]
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_llave_cierra",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 44: #,
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_coma",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 10: #salto de linea
        fila += 1
        columna = 0
        valor = ""
    elif ord(c) == 32: #espacio
        columna += 1
        valor = ""
    else: 
        mostrarError(c,"",fila,columna)

def automataObjeto(s):
    global temp,tablaAtributos,estado,flagAutomataObjeto
    if estado == 0:
        if s.token == "ID":
            temp = Atributo(s.lexema,"")
            estado = 1
        else:
            estado = -1
            flagAutomataObjeto = False
            mostrarError(s.lexema,"ID",s.linea,s.columna) 
    elif estado == 1:
        if s.token == "simbolo_igual":
            estado = 2
        else:
            estado = -1
            flagAutomataObjeto = False
            mostrarError(s.lexema,"=",s.linea,s.columna)
    elif estado == 2:
        if s.token == "CADENA":
            estado = 3
            temp.valor = s.lexema
            tablaAtributos.append(temp)
            temp = None
        else:
            estado = -1
            flagAutomataObjeto = False
            mostrarError(s.lexema,"CADENA",s.linea,s.columna)
    elif estado == 3:
        if s.token == "simbolo_coma":
            estado = 0
        elif s.token == "simbolo_llave_cierra": #estado de aceptacion
            estado = 0
            flagAutomataObjeto = False
        else:
            estado = -1
            flagAutomataObjeto = False
            mostrarError(s.lexema,"] o ,",s.linea,s.columna)

cadena = "[id1 = \"valor1\",id2 = \"valor2\"] \n [ id3 = \"valor3\", id4 = \"valor4\"]"
caracteres = list(cadena)

for c in caracteres:
    analizadorLexico(c)

for s in tablaSimbolos:
    
    if flagAutomataObjeto:
        automataObjeto(s)
    elif s.token == "simbolo_llave_abre":
        estado = 0
        flagAutomataObjeto = True
    else:
        mostrarError(s.lexema,"[",s.linea,s.columna)

for a in tablaAtributos:
    print(a.id + ": " + a.valor)

