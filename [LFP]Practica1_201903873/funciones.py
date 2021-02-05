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

def Buscar(Lista, x):
    if x in Lista:
        for i in range(0,len(Lista)):
            if Lista[i]==x:
                return str(i+1)
    else:
        return 'Valor no encontrado'



def Ordenada(linea):
    if linea[2]=='ORDENAR':
        lineas = linea[1].split(',')
        line = Ordenar(lineas)
        string = ",".join(line)
        f = linea[0]+': '+ linea[1] +' | Resultado de Ordenar: '+ string + '\n'
        print(f)
    else: 
        return -1

def Buscada(linea):
    if linea[2]=='BUSCAR':
        line = linea[3].split(',')
        lineas = linea[1].split(',')
        s = ','.join(lineas)
        for i in range(0,len(line)):
            j=line[i]
            l=Buscar(lineas, j)
            f = linea[0]+': '+ s +'| Valor Buscado: '+ j +'| Encontrado en la posición: '+ l + '\n' 
            print(f)
    else:
        return -1

def TodasOrdenar(linea):
    if linea[2]=='ORDENAR,BUSCAR':
        Ordenada(linea)
        
    else:
        return -1

def TodasBuscar(linea):
    if linea[2]=='ORDENAR,BUSCAR':
        
        Buscada(linea)
    else:
        return -1

def Todas(linea):
    if linea[2]=='ORDENAR,BUSCAR':
        Buscada(linea)
    else:
        return -1









        


    


