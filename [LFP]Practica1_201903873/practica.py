import funciones
import sys

funciones.Menu()
while True:
    
    n = input('Ingrese valor \n')

    if n=='1':
        j = funciones.abrirArchivo()
        for linea in j:
            i = funciones.accion(linea)
            print(i)
        funciones.Menu()
    elif n=='2': 
        print('Listas Ordenadas')
        funciones.Menu()   
    elif n=='3': 
        print('Busquedas')
        funciones.Menu()  
    elif n=='4':
        print('Todas')
        funciones.Menu()    
    elif n=='5':
        print('Todas a Archivos')
        funciones.Menu()
    elif n=='6':
        print('Carné:201903873')
        print('Nombre:Joaquin Emmanuel Aldair Coromac Huezo')
        print('Correo Electrónico: jeach.27@gmail.com')
        print('Curso: Laboratorio Lenguajes Formales y de Programación')
        n = input("Pulsa la tecla 's' para salir\n")
        if n=='s':
            sys.exit()
            
    else:
        print ("No has pulsado una opción correcta")
    