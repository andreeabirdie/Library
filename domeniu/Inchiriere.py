'''
Created on 3 Dec 2018

@author: Birdie
'''
from domeniu.Carte import Carte
from domeniu.Client import Client

class Inchiriere():
    
    def __init__(self,carte,client):
        self.__carte = carte
        self.__client = client
        
        
    def getCarte(self):
        return self.__carte
    
    '''
    def getIdCarte(self):
        return self.__carte.getId()
        print(self.__carte.getId())
    '''
        
    def setCarte(self,carte):
        self.__carte = carte
        
    def getClient(self):
        return self.__client
    
    def setClient(self,client):
        self.__client = client
        
    def __str__(self):
        return 'Cartea cu id: ' + str(self.__carte.getId()) + ' a fost inchiriata de clientul cu id: ' + str(self.__client.getId())
      
    def __eq__(self,altaValoare):  
        if type(altaValoare) == Carte:
            return self.__carte == altaValoare
        elif type(altaValoare) == Client:
            return self.__client == altaValoare
        else:
            return self.__carte == altaValoare.__carte and self.__client == altaValoare.__client