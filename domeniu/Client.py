class Client:
    
    '''
    obiecte de tip client
    '''
    
    def __init__(self, ID, nume, cnp):
        self.__ID = ID
        self.__nume = nume
        self.__cnp = cnp
        
    def getId(self):
        return self.__ID
    
    def setId(self, ID):
        self.__ID = ID
        
    def getNume(self):
        return self.__nume
    
    def setNume(self, nume):
        self.__nume = nume
        
    def getCnp(self):
        return self.__cnp
    
    def setCnp(self,cnp):
        self.__cnp = cnp
        
    def __str__(self):
        return 'id: ' + str(self.__ID) + ' nume: ' + self.__nume + ' cnp: ' + str(self.__cnp)
    
    def __eq__(self,client):
        '''
        '''
        return self.__ID == client.__ID
        