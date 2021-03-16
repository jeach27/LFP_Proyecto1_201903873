import webbrowser
import os

def generarHTML_MS(simbolos,Limite):
    f = open('MenuSimbolos.html','w')
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
    f.write('<div class="card text-center">\n')
    f.write('<div class="card-body">\n')
    for a in range(len(simbolos)):
        s = simbolos[a]
        if s.tipo == 'CADENA':
            if a == 1:
                f.write('<h1><span class="badge bg-secondary">'+str(s.lexema)+'</span></h1>\n')
            else:
                f.write('<h4>'+str(s.lexema)+'</h4>\n')
        elif s.tipo == 'NombreSeccion':
            f.write('<h2><span class="badge bg-secondary">'+str(s.lexema)+'</span></h2>\n')
        elif s.tipo == 'Identificador':
            f.write('\n')
        elif s.tipo == 'NUMERO':
            f.write('<h4>'+str(s.lexema)+'</h4>\n')

    f.write('</div>\n')
    f.write('</div>\n')
        
    f.write('       <nav aria-label="...">\n')
    f.write('           <ul class="pagination pagination-lg">\n')
    f.write('               <li class="page-item active" aria-current="page">\n')
    f.write('                   <span class="page-link">1</span>\n')
    f.write('               </li>\n')
    f.write('               <li class="page-item"><a class="page-link" href="TablaMenuSimbolos.html">2</a></li>\n')
    f.write('           </ul>\n')
    f.write('       </nav>\n')
   
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

def generarHTML_FS(simbolosF,atributosM):
    f = open('FacturaSimbolos.html','w')
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
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('FacturaSimbolos.html')

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

def crearNodo(identificador, nombre , shape):
    return identificador + '[label="'+ nombre +'",shape="'+ shape +'"]\n'

def generarArbol(simbolos):
    
    file = open('arbolMenu.dot','w')
    file.write('digraph G{\n')
    for i in range(len(simbolos)):
        s = simbolos[i]
        if i == 1:
            file.write('A[label="'+s.lexema+'", shape="circle"]\n')
        elif s.tipo == 'NombreSeccion':
            file.write(crearNodo(str(s),str(s.lexema),"circle"))
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
                    file.write(crearNodo(str(a),cadena+numero+'\n'+str(a.lexema),"box"))
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
