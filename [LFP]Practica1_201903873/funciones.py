from tkinter import filedialog

def Menu():
    print('---------Menu principal-------------')
    print('Elija una opcion')
    print('1.Cargar Archivo\n2.Desplegar Listas Ordenadas\n3.Desplegar Búsquedas\n4.Desplegar Todas\n5.Desplegar Todas a Archivo\n6.Salir')

def abrirArchivo():
    archivo = filedialog.askopenfile( title = 'Cargar Archivo', filetypes = (('txt files','*.txt'),('all files','*.')))
    return archivo

def accion(linea):
    linea = linea.rstrip('\n')
    linea = linea.replace('=',' ')
    dividida = linea.split(' ')
    return dividida
    
def Ordenar(Lista):
    for no in range(len(Lista)-1,0,-1):
        for i in range(no):
            if Lista[i]>Lista[i+1]:
                temp = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temp

def Buscar(x, Lista):
    try:
        indice = Lista.index(x)
        print('El número esta en la posición {}'.format(indice))
    except:
        print('El número no se encuentra en la lista')




