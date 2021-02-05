import funciones
import sys

def Menu():
    lista=list()
    while True:
        print('\n-----------Menu principal---------------')
        print('\n> Elija una opcion')
        print('\n1.Cargar Archivo\n2.Desplegar Listas Ordenadas\n3.Desplegar Búsquedas\n4.Desplegar Todas\n5.Desplegar Todas a Archivo\n6.Salir')
        n=input('\n> Ingrese valor\n')
        if n=='1':
            if lista:
                lista.clear()
                j=funciones.abrirArchivo()
                for linea in j:
                    funciones.accion(linea, lista)
            else:
                j=funciones.abrirArchivo()
                for linea in j:
                    funciones.accion(linea, lista)
            
            print('\nEl archivo fue cargado correctamente\n')  
            print(lista) 
                
        # funciones.Menu()
        elif n=='2': 
            print('---------------Listas Ordenadas-------------\n')
            for i in range(0,len(lista)):
                j=lista[i]
                funciones.Ordenada(j)        
            #funciones.Menu()   
        elif n=='3': 
            print('-------------------Busquedas-------------------\n')
            for i in range(0,len(lista)):
                j=lista[i]
                funciones.Buscada(j)
            #funciones.Menu()  
        elif n=='4':
            print('---------------------Todas------------------------\n')
            for i in range(0,len(lista)):
                j=lista[i]
                
                funciones.Buscada(j)
                funciones.Ordenada(j)
        # funciones.Menu()    
        elif n=='5':
            print('Todas a Archivos')
        # funciones.Menu()
        elif n=='6':
            print('--------------------Datos--------------------------')
            print('\nCarné:201903873')
            print('Nombre:Joaquin Emmanuel Aldair Coromac Huezo')
            print('Correo Electrónico: jeach.27@gmail.com')
            print('Curso: Laboratorio Lenguajes Formales y de Programación')
            n = input("\n----> Pulsa la tecla 's' para salir\n")
            if n=='s':
                sys.exit()
                
        else:
            print ("No has pulsado una opción correcta")
        
            



