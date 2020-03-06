class Carte:
    
    '''
    obiecte de tip carte
    '''
    
    def __init__(self, ID, titlu, descriere, autor):
        self.__ID = ID
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
        
    def getId(self):
        return self.__ID
    
    def setId(self, ID):
        self.__ID = ID
        
    def getTitlu(self):
        return self.__titlu
    
    def setTitlu(self, titlu):
        self.__titlu = titlu
        
    def getDescriere(self):
        return self.__descriere
    
    def setDescriere(self, descriere):
        self.__descriere = descriere
        
    def getAutor(self):
        return self.__autor
    
    def setAutor(self, autor):
        self.__autor = autor
        
    def __str__(self):
        return 'id: ' + str(self.__ID) + ' titlu: ' + str(self.__titlu) + ' autor: ' + str(self.__autor) + ' descriere: ' + str(self.__descriere)
    
    def __eq__(self,altaCarte):
        '''
        id egal
        '''
        return self.__ID == altaCarte.__ID
        
        