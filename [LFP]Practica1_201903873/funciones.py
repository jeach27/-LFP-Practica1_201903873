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
    posiciones=list()
    for i in range(0,len(Lista)):
        if Lista[i]==x:
            j=str(i+1)
            posiciones.append(j)
    return posiciones

def Ordenada(linea):
    if linea[2]=='ORDENAR':
        lineas = linea[1].split(',')
        line = Ordenar(lineas)
        string = ",".join(line)
        f = linea[0]+': '+ linea[1] +' | Resultado de Ordenar: '+ string + '\n'
        return f
    else: 
        return -1

def Buscada(linea):
    posiciones=list()
    if linea[2]=='BUSCAR':
        line = linea[3].split(',')#line= lista de numeros a encontrar
        lineas = linea[1].split(',')#lineas=lista de numeros donde encontrar
        s = ','.join(lineas)#vuelve la lista de números en un string
        j = ''
        for i in range(0, len(line)):
            j = line[i]   
            posiciones = Buscar(lineas, j)
        if posiciones:
            h = ','.join(posiciones)
            f = linea[0]+': '+ s +'| Valor Buscado: '+ j +'| Encontrado en la posición: '+ h + '\n'
        else:     
            f = linea[0]+': '+ s +'| Valor Buscado: '+ j +'| Encontrado en la posición: '+ 'Valor no Encontrado' + '\n'

        return f
    else:
        return -1    

def TodasOrdenar(linea):
    if linea[2]=='ORDENAR,BUSCAR':
        lineas = linea[1].split(',')
        line = Ordenar(lineas)
        string = ",".join(line)
        f = linea[0]+': '+ linea[1] +' | Resultado de Ordenar: '+ string + '\n'
        return f
        
    else:
        return -1

def TodasBuscar(linea):
    posiciones=list()
    if linea[2]=='ORDENAR,BUSCAR':
        line = linea[3].split(',')
        lineas = linea[1].split(',')
        s = ','.join(lineas)
        for i in range(0,len(line)):
            j = line[i]   
            posiciones = Buscar(lineas, j)
        if posiciones:
            h = ','.join(posiciones)
            f = linea[0]+': '+ s +'| Valor Buscado: '+ j +'| Encontrado en la posición: '+ h + '\n'
        else:
            f = linea[0]+': '+ s +'| Valor Buscado: '+ j +'| Encontrado en la posición: '+ 'Valor no Encontrado' + '\n'
        return f    

    else:
        return -1

def Todas(lista):
    x = Buscada(lista)
    if x!= -1:
        print(x)
    y = Ordenada(lista)
    if y!= -1:
        print(y)
    z = TodasBuscar(lista)
    if z!= -1:
        print(z)
    c = TodasOrdenar(lista)
    if c!= -1:
        print(c)

def TodasArchivos(lista):
    x = Buscada(lista)
    if x!= -1:
        print(x)
    y = Ordenada(lista)
    if y!= -1:
        print(y)
    z = TodasBuscar(lista)
    if z!= -1:
        print(z)
    c = TodasOrdenar(lista)
    if c!= -1:
        print(c)










        


    


