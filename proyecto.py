import sys

def menu():
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
        elif n=='2':
            print('--------------Cargar Orden-----------')
        elif n=='3':
            print('-------------Generar Menú------------')
        elif n=='4':
            print('------------Generar Factura-------------')
        elif n=='5':
            print('-----------Generar Árbol--------------')
        elif n=='6':
            print('------------Salir-------------')
            print('\n----> Pulsa una tecla para salir\n')
            input("")
            sys.exit()
        else:
            print ("No has pulsado una opción correcta")