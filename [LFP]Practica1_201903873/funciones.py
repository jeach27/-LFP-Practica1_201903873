from tkinter import filedialog

def Menu():
    
    print('---------Menu principal-------------')
    print('Elija una opcion')
    print('1.Cargar Archivo\n2.Desplegar Listas Ordenadas\n3.Desplegar Búsquedas\n4.Desplegar Todas\n5.Desplegar Todas a Archivo\n6.Salir')

def abrirArchivo():
    archivo = filedialog.askopenfile( title = 'Cargar Archivo', filetypes = (('txt files','*.txt'),('all files','*.')))
    return archivo

def accion(linea,lista):
    linea = linea.rstrip('\n')
    linea = linea.replace('=',' ')
    dividida = linea.split(' ')
    lista.append(dividida)
    
    
def Ordenar(Lista):
    for no in range(len(Lista)-1,0,-1):
        for i in range(no):
            if Lista[i]>Lista[i+1]:
                temp = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temp
    return Lista

def Buscar(x, Lista):
    try:
        indice = Lista.index(x)
        return indice
    #    print('El número esta en la posición {}'.format(indice))
    except:
        return -1
    #    print('El número no se encuentra en la lista')

def Ordenada(linea):
    if linea[2]=='ORDENAR':
        lineas = linea[1].split(',')
        line = Ordenar(lineas)
        string = ",".join(line)
        s = ','.join(lineas)
        f = linea[0]+': '+ s +' | Resultado de Ordenar: '+ string
        print(f)

def Buscada(linea, x):
    if linea[2]=='BUSCAR':
        line = linea[3].split(',')
        print(line)


    


