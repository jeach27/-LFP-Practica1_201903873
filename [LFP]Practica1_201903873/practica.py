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
            
            print('\n--> El archivo fue cargado correctamente\n')  
            #print(lista) 
                
        elif n=='2': 
            print('---------------Listas Ordenadas-------------\n')
            for i in range(0,len(lista)):
                j=lista[i]
                x = funciones.Ordenada(j)
                y = funciones.TodasOrdenar(j) 
                if x != -1:
                    print(x) 
                if y != -1:
                    print(y)     
               
        elif n=='3': 
            print('-------------------Busquedas-------------------\n')
            for i in range(0,len(lista)):
                j=lista[i]
                x = funciones.Buscada(j)
                y = funciones.TodasBuscar(j)
                if x != -1:
                    print(x) 
                if y != -1:
                    print(y)
              
        elif n=='4':
            print('---------------------Todas------------------------\n')
            
            for i in range(0,len(lista)):
                j=lista[i]
                funciones.Todas(j)
            
        elif n=='5':
            Final=list()
            print('Todas a Archivos')
            for i in range(0,len(lista)):
                j=lista[i]
                Final.append(funciones.TodasArchivos(j))
            funciones.archivo(Final)
        
        elif n=='6':
            print('--------------------Datos--------------------------')
            print('\nCarné:201903873')
            print('Nombre:Joaquin Emmanuel Aldair Coromac Huezo')
            print('Correo Electrónico: jeach.27@gmail.com')
            print('Curso: Laboratorio Lenguajes Formales y de Programación')
            print('\n----> Pulsa una tecla para salir\n')
            input("")
            sys.exit()
                
        else:
            print ("No has pulsado una opción correcta")
        
            



