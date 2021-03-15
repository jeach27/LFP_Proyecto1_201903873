import sys
import tkinter 
from tkinter import filedialog
import analizadorMenu
import analizadorOrden
import funciones

def CargarArchivo():
    archivo = filedialog.askopenfilename(title = 'Cargar Archivo', filetypes = (('lfp files','*.lfp'),('all files','*.')))
    return archivo

def menu():
    menu = None
    orden = None
    SimboloMenu = None
    while True:
        print('\n-----------Proyecto 1----LFP---------- ')
        print('\nCarné:201903873')
        print('Nombre:Joaquin Emmanuel Aldair Coromac Huezo')
        print('Correo Electrónico: jeach.27@gmail.com')
        print('Curso: Laboratorio Lenguajes Formales y de Programación')
        print('\n1.Cargar Menú')
        print('2.Cargar Orden')
        print('3.Generar Menú')
        print('4.Generar Factura')
        print('5.Generar Árbol')
        print('6.Salir')
        n=input('\n> Ingrese una opción\n')

        if n=='1': 
            print('-----------Cargar Menú--------------') 
            menu = CargarArchivo()
            if menu != None:
                print('\n-> Se ha cargado el archivo Menú correctamente')

        elif n=='2':
            print('--------------Cargar Orden-----------')
            orden = CargarArchivo()
            if orden != None:
                print('\n-> Se ha cargado el archivo Orden correctamente')

        elif n=='3':
            print('-------------Generar Menú------------')
            if menu != None:
                j = input('\nDesea límite de precio en el Menú\n1.Si\n2.No\n')
                if j =='1':
                    limite = float(input('Ingrese limite de precio\n'))
                elif j=='2':
                    limite = -1
                else:
                    print('dato ingresado incorrecto')
                archivoss = menu
                with open(archivoss,'r',encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    SimboloMenu = analizadorMenu.ingreso(contenido,limite)
                    
            else:
                print('\n-> No se ha cargado un archivo Menú')

        elif n=='4':
            print('------------Generar Factura-------------')
            if orden != None:
                archiv = orden
                with open(archiv,'r',encoding='utf-8') as archivos:
                    contenid = archivos.read()
                    analizadorOrden.ingreso(contenid)
                    
            else:
                print('\n-> No se ha cargado un archivo Orden')

        elif n=='5':
            print('-----------Generar Árbol--------------')
            funciones.generarArbol(SimboloMenu)

        elif n=='6':
            print('------------Salir-------------')
            print('\n----> Pulsa una tecla para salir\n')
            input("")
            sys.exit()

        else:
            print ("No has pulsado una opción correcta")


