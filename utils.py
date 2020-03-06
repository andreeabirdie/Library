
def SelectionSort(lista, key = lambda x:x, reverse=False):
    '''
    Functie care foloseste metoda de sortare prin selectie pentru a sorta o lista data
    input:lista ce trebuie sortata
    output:lista sortata
    '''

    for i in range(0,len(lista)-1):
        elementul_minim = lista[i]
        elementul_maxim = lista[i]
        index_element_minim = i
        index_element_maxim = i
        for j in range(i+1,len(lista)):
            if key(lista[j])<key(elementul_minim):
                index_element_minim = j 
                elementul_minim = lista[j]
            if key(lista[j])>key(elementul_maxim):
                index_element_maxim = j 
                elementul_maxim = lista[j]
        
        if not reverse:
            lista[index_element_minim] = lista[i]
            lista[i] = elementul_minim
        
        if reverse:
            lista[index_element_maxim] = lista[i]
            lista[i] = elementul_maxim

    return lista

def ShakerSort(lista,key = lambda x:x,reverse = False):
    '''
    Functie care sorteaza o lista folosind metoda de shake sort pentru a sorta o lista data
    input:lista ce trebuie sortata
    output: lista sortata
    '''
    capat_stanga = 0
    capat_dreapta = len(lista) -1
    listaNesortata = True
    
    while(listaNesortata):
        listaNesortata = False
        for i in range(capat_stanga,capat_dreapta):
            if not reverse:
                if key(lista[i])>key(lista[i+1]):
                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = auxiliar
                    listaNesortata = True
            else:
                if key(lista[i])<key(lista[i+1]):
                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = auxiliar
                    listaNesortata = True
                
        if listaNesortata == False:
            break
        
        listaNesortata = False
        capat_dreapta -= 1
        
        for i in range(capat_dreapta,capat_stanga,-1):
            if not reverse:
                if key(lista[i])<key(lista[i-1]):
                    auxiliar = lista[i]
                    lista[i] = lista[i-1]
                    lista[i-1] = auxiliar
                    listaNesortata = True
            
            else: 
                if key(lista[i])>key(lista[i-1]):
                    auxiliar = lista[i]
                    lista[i] = lista[i-1]
                    lista[i-1] = auxiliar
                    listaNesortata = True
                
        capat_stanga += 1
        
    return lista