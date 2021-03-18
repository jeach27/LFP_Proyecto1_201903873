import webbrowser
import os
from datetime import datetime

def sumaLista(lista):
    suma = 0
    for i in lista:
        i = float(i)
        suma = suma + i
    return suma

def generarHTML_MS(simbolos,Limite):
    f = open('MenuSimbolos.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Menu</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')

    f.write('<div class="container-fluid">\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')

    for a in range(len(simbolos)):
        s = simbolos[a]
        if s.tipo == 'CADENA':
            if a == 1:
                f.write('<h2 class="text-center">'+str(s.lexema)+'</h2>\n')
                break
    
    f.write('</div>\n')
    f.write('</div>\n')
    
    for i in range(len(simbolos)):
        s = simbolos[i]
        if s.tipo == 'NombreSeccion':
            f.write('<div class="row-center">\n')
            f.write('<div class="col-md-12">\n')
            f.write('<h3 class="text-left">	'+str(s.lexema)+'</h3>\n')
            Secciones = list()
            for j in range(i+1,len(simbolos)):
                sim = simbolos[j]
                if sim.tipo == 'NombreSeccion':
                    break
                elif sim.tipo == 'Identificador':
                    pass
                else:
                    Secciones.append(sim)
            contador = 0
            cadena = None
            numero = None
            for a in Secciones:
                contador += 1
                if contador == 1:
                    cadena = str(a.lexema)
                if contador == 2:
                    numero = float(a.lexema)
                    numero = round(numero,2)
                    numero = str(numero)
                if contador == 3:
                    if Limite == -1:
                        f.write('<div class="row">\n')
                        f.write('<div class="col-md-6"><h4 class="text-primary">'+cadena+'</h4></div>\n')
                        f.write('<div class="col-md-6"><h4 class="text-primary">Q '+numero+'</h4></div>\n')
                        f.write('</div>\n')
                        f.write('<div class="row-center">\n')
                        f.write('<div class="col-md-12">	<h5 class="text-muted">'+str(a.lexema)+'</h5>	</div>\n')
                        f.write('</div>\n')
                    else:
                        if float(numero) < Limite:
                            f.write('<div class="row">\n')
                            f.write('<div class="col-md-6"><h4 class="text-primary">'+cadena+'</h4></div>\n')
                            f.write('<div class="col-md-6"><h4 class="text-primary">Q '+numero+'</h4></div>\n')
                            f.write('</div>\n')
                            f.write('<div class="row-center">\n')
                            f.write('<div class="col-md-12">	<h5 class="text-muted">'+str(a.lexema)+'</h5>	</div>\n')
                            f.write('</div>\n')
                    contador = 0
                    cadena = None
                    numero = None
            f.write('</div>\n')
            f.write('</div>\n')

    f.write('</div>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('<script src="js/jquery.min.js"></script>\n')
    f.write('<script src="js/bootstrap.min.js"></script>\n')
    f.write('<script src="js/scripts.js"></script>\n')
    
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    f.write('       <nav aria-label="...">\n')
    f.write('           <ul class="pagination pagination-lg">\n')
    f.write('               <li class="page-item active" aria-current="page">\n')
    f.write('                   <span class="page-link">1</span>\n')
    f.write('               </li>\n')
    f.write('               <li class="page-item"><a class="page-link" href="TablaMenuSimbolos.html">2</a></li>\n')
    f.write('           </ul>\n')
    f.write('       </nav>\n')
    f.write('</div>\n')
    f.write('</div>\n')

    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('MenuSimbolos.html')

    f = open('TablaMenuSimbolos.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Tabla Simbolos Menu</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    f.write('       <table class="table table-striped table-dark">\n')
    f.write('       <thead>\n')
    f.write('           <tr>\n')
    f.write('               <th scope="col">No</th>\n')   
    f.write('               <th scope="col">Lexema</th>\n')
    f.write('               <th scope="col">Fila</th>\n')
    f.write('               <th scope="col">Columna</th>\n')
    f.write('               <th scope="col">Token</th>\n')
    f.write('           </tr>\n')
    f.write('       </thead>\n')
    f.write('       <tbody>\n')

    for e in range(len(simbolos)):
        j = simbolos[e]
        f.write('           <tr>\n')
        f.write('               <th scope="row">'+str(e+1)+'</th>\n')
        f.write('                   <td>'+str(j.lexema)+'</td>\n')
        f.write('                   <td>'+str(j.fila)+'</td>\n')
        f.write('                   <td>'+str(j.columna)+'</td>\n')
        f.write('                   <td>'+j.tipo+'</td>\n')
        f.write('           </tr>\n')
        
    f.write('       </tbody>\n')
    f.write('       </table>\n')
    f.write('       <nav aria-label="...">\n')
    f.write('           <ul class="pagination pagination-lg">\n')
    f.write('               <li class="page-item"><a class="page-link" href="MenuSimbolos.html">1</a></li>\n')
    f.write('               <li class="page-item active" aria-current="page">\n')
    f.write('                   <span class="page-link">2</span>\n')
    f.write('               </li>\n')
    f.write('           </ul>\n')
    f.write('       </nav>\n')
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    #webbrowser.open_new_tab('TablaMenuSimbolos.html')

def generarHTML_MER(errores):
    f = open('ErroresMenu.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Tabla Errores Menu</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    f.write('       <table class="table table-striped table-dark">\n')
    f.write('       <thead>\n')
    f.write('           <tr>\n')
    f.write('               <th scope="col">No</th>\n')   
    f.write('               <th scope="col">Lexema</th>\n')
    f.write('               <th scope="col">Descripcion</th>\n')
    f.write('               <th scope="col">Fila</th>\n')
    f.write('               <th scope="col">Columna</th>\n')
    f.write('           </tr>\n')
    f.write('       </thead>\n')
    f.write('       <tbody>\n')

    for e in range(len(errores)):
        j = errores[e]
        f.write('           <tr>\n')
        f.write('               <th scope="row">'+str(e+1)+'</th>\n')
        f.write('               <td>'+str(j.lexema)+'</td>\n')
        f.write('               <td>'+j.descripcion+'</td>\n')
        f.write('               <td>'+str(j.fila)+'</td>\n')
        f.write('               <td>'+str(j.columna)+'</td>\n')
        f.write('           </tr>\n')
        
    f.write('       </tbody>\n')
    f.write('       </table>\n')
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('ErroresMenu.html')

def generarHTML_FS(simbolosF,atributosM,contador):
    subtotal = list()
    sub = 0
    prop = 0
    total = 0
    now = datetime.now()
    f = open('FacturaSimbolos.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Factura</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    f.write('<div class="container-fluid">\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    for i in atributosM:
        if i.tipo == 'CADENA':
            f.write('<h3 class="text-center">FACTURA '+ str(i.lexema) +'</h3>\n')
            break
    f.write('<h5 class="text-center">Factura No.'+ str(contador)+ ' </h5>\n')
    f.write('<h5 class="text-center"> Fecha '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'</h5>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    f.write('<h4 class="text-left">Datos del Cliente </h4>\n')
    for s in range(len(simbolosF)):
        sim = simbolosF[s]
        if s == 0:
            f.write('<h5 class="text-left">Nombre:  '+str(sim.lexema)+'</h5>  \n')
        elif s == 1:
            f.write('<h5 class="text-left">Nit:  '+str(sim.lexema)+'</h5>\n')
        elif s == 2:
            f.write('<h5 class="text-left">Direccion:  '+str(sim.lexema)+'</h5>\n')
            break
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    f.write('<table class="table table-bordered">\n')
    f.write('<thead>\n')
    f.write('<tr> <th> Descripcion </th> </tr>\n')
    f.write('<tr>\n')
    f.write('<th>	Cantidad	</th>\n')
    f.write('<th> Identificador	</th>\n')
    f.write('<th>	Precio	</th>\n')
    f.write('<th>	Total	</th>\n')
    f.write('</tr>\n')
    f.write('</thead>\n')
    f.write('<tbody>\n')
    for j in range(len(simbolosF)):
        sim = simbolosF[j]
        if sim.tipo == 'NUMERO':
            cantidad = sim.lexema
            cantidad = float(cantidad)
            cantidad = round(cantidad, 2)
            identificador = simbolosF[j+1].lexema
            for i in range(len(atributosM)):
                s = atributosM[i]
                if s.lexema == identificador:
                    precio = atributosM[i+2].lexema
                    precio = float(precio)
                    precio = round(precio , 2)
                    total = int(cantidad)*float(precio)
                    total = round(total,2)
                    subtotal.append(total)
                    f.write('<tr>\n')
                    f.write('<td>'+str(cantidad)+'</td>\n')
                    f.write('<td>'+str(identificador)+'</td>\n')
                    f.write('<td>Q '+str(precio)+'</td>\n')
                    f.write('<td>Q '+str(total)+'</td>\n')
                    f.write('</tr>\n')
                    break
    f.write('</tbody>\n')
    f.write('</table>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    sub = float(sumaLista(subtotal))
    sub = round(sub ,2)
    f.write('<h4 class="text-right">Subtotal ----------------------- Q '+str(sub)+'</h4>\n')
    
    for i in simbolosF:
        if i.tipo == 'Porcentaje':
            porc = float(i.lexema)
            porc = round(porc , 2)
            prop = sub * porc / 100
            prop = round(prop ,2)
            f.write('<h4 class="text-right">Propina ('+str(porc)+'%)--------------------Q '+str(prop)+'</h4>\n')
            break
    
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('<div class="row">\n')
    f.write('<div class="col-md-12">\n')
    total = sub + prop
    total = round(total ,2)
    f.write('<h4 class="text-right">Total ----------------------- Q '+str(total)+'</h4>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('<script src="js/jquery.min.js"></script>\n')
    f.write('<script src="js/bootstrap.min.js"></script>\n')
    f.write('<script src="js/scripts.js"></script>\n')    

    f.write('       <nav aria-label="...">\n')
    f.write('           <ul class="pagination pagination-lg">\n')
    f.write('               <li class="page-item active" aria-current="page">\n')
    f.write('                   <span class="page-link">1</span>\n')
    f.write('               </li>\n')
    f.write('               <li class="page-item"><a class="page-link" href="TablaFacturaSimbolos.html">2</a></li>\n')
    f.write('           </ul>\n')
    f.write('       </nav>\n')
   
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('FacturaSimbolos.html')

    f = open('TablaFacturaSimbolos.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Tabla Simbolos Factura</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    f.write('       <table class="table table-striped table-dark">\n')
    f.write('       <thead>\n')
    f.write('           <tr>\n')
    f.write('               <th scope="col">No</th>\n')   
    f.write('               <th scope="col">Lexema</th>\n')
    f.write('               <th scope="col">Fila</th>\n')
    f.write('               <th scope="col">Columna</th>\n')
    f.write('               <th scope="col">Token</th>\n')
    f.write('           </tr>\n')
    f.write('       </thead>\n')
    f.write('       <tbody>\n')

    for e in range(len(simbolosF)):
        j = simbolosF[e]
        f.write('           <tr>\n')
        f.write('               <th scope="row">'+str(e+1)+'</th>\n')
        f.write('               <td>'+str(j.lexema)+'</td>\n')
        f.write('               <td>'+str(j.fila)+'</td>\n')
        f.write('               <td>'+str(j.columna)+'</td>\n')
        f.write('               <td>'+j.tipo+'</td>\n')
        f.write('           </tr>\n')
        
    f.write('       </tbody>\n')
    f.write('       </table>\n')
    f.write('       <nav aria-label="...">\n')
    f.write('           <ul class="pagination pagination-lg">\n')
    f.write('               <li class="page-item"><a class="page-link" href="FacturaSimbolos.html">1</a></li>\n')
    f.write('               <li class="page-item active" aria-current="page">\n')
    f.write('                   <span class="page-link">2</span>\n')
    f.write('               </li>\n')
    f.write('           </ul>\n')
    f.write('       </nav>\n')
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()
    #webbrowser.open_new_tab('TablaFacturaSimbolos.html')

def generarHTML_FER(errores):
    f = open('ErroresFactura.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Tabla Errores Factura</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    f.write('       <table class="table table-striped table-dark">\n')
    f.write('       <thead>\n')
    f.write('           <tr>\n')
    f.write('               <th scope="col">No</th>\n')   
    f.write('               <th scope="col">Lexema</th>\n')
    f.write('               <th scope="col">Descripcion</th>\n')
    f.write('               <th scope="col">Fila</th>\n')
    f.write('               <th scope="col">Columna</th>\n')
    f.write('           </tr>\n')
    f.write('       </thead>\n')
    f.write('       <tbody>\n')
    for e in range(len(errores)):
        j = errores[e]
        f.write('           <tr>')
        f.write('               <td>'+str(e+1)+'</td>\n')
        f.write('               <td>'+str(j.lexema)+'</td>\n')
        f.write('               <td>'+j.descripcion+'</td>\n')
        f.write('               <td>'+str(j.fila)+'</td>\n')
        f.write('               <td>'+str(j.columna)+'</td>\n')
        f.write(            '</tr>')
    f.write('       </tbody>')
    f.write('       </table>')
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('ErroresFactura.html')

def unirNodo(NodoA ,NodoB):
    return NodoA + '->' + NodoB + '\n'

def crearNodo(identificador, nombre , shape, color):
    return identificador + '[label="'+ nombre +'",shape="'+ shape +'",fillcolor='+color+']\n'

def generarArbol(simbolos):
    
    file = open('arbolMenu.dot','w')
    file.write('digraph G{\n')
    for i in range(len(simbolos)):
        s = simbolos[i]
        if i == 1:
            file.write('A[label="'+s.lexema+'", shape="oval", fillcolor="lightsteelblue1"]\n')
        elif s.tipo == 'NombreSeccion':
            file.write(crearNodo(str(s),str(s.lexema),"ellipse","deepskyblue"))
            Secciones = list()
            for j in range(i+1,len(simbolos)):
                sim = simbolos[j]
                if sim.tipo == 'NombreSeccion':
                    break
                elif sim.tipo == 'Identificador':
                    pass
                else:
                    Secciones.append(sim)
            contador = 0
            cadena = None
            numero = None
            for a in Secciones:
                contador += 1
                if contador == 1:
                    cadena = str(a.lexema)
                if contador == 2:
                    numero = float(a.lexema)
                    numero = round(numero,2)
                    numero = str(numero)
                if contador == 3:
                    file.write(crearNodo(str(a),'{ { '+cadena+' | '+'Q '+numero+' | '+str(a.lexema)+' } }',"Mrecord","lightslateblue"))
                    contador = 0
                    cadena = None
                    numero = None

    for i in range(len(simbolos)):
        s = simbolos[i]
        
        if s.tipo == 'NombreSeccion':
            file.write(unirNodo("A",str(s)))
            Secciones = list()
            for j in range(i+1,len(simbolos)):
                sim = simbolos[j]
                if sim.tipo == 'NombreSeccion':
                    break
                elif sim.tipo == 'Identificador':
                    pass
                else:
                    Secciones.append(sim)
            contador = 0
            cadena = None
            numero = None
            for a in Secciones:
                contador += 1
                if contador == 1:
                    cadena = str(a.lexema)
                if contador == 2:
                    numero = str(a.lexema)
                if contador == 3:
                    file.write(unirNodo(str(s),str(a)))
                    contador = 0
                    cadena = None
                    numero = None
     
    file.write('}')
    file.close()
    os.system('dot -Tpng arbolMenu.dot -o arbolMenu.jpg')
    os.startfile('arbolMenu.jpg')
