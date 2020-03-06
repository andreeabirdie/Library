'''
Created on 9 Dec 2018

@author: Birdie
'''
from Repository.Repository import Repository
from domeniu.Client import Client
from Validator.Exceptii import RepositoryException

class ClientFileRepositoryNoMemory(Repository):
    
    def __init__(self,nume_fisier):
        self.__nume_fisier = nume_fisier
        
    def __citesteDinFisier(self):
        '''
        Incarca datele din fisier in memorie
        '''
        try:
            fisier = open(self.__nume_fisier,"r")
        except IOError:
            return []
        linieDinFisier = fisier.readline().strip()
        clienti = []
        while linieDinFisier != "":
            cuvinte = linieDinFisier.split(',')
            clienti.append(Client(cuvinte[0],cuvinte[1],int(cuvinte[2])))
            linieDinFisier = fisier.readline().strip()
        fisier.close()
        return clienti
    
    def __scrieInFisier(self,clienti):
        '''
        Incarca datele din memorie in fisier
        '''
        fisier = open(self.__nume_fisier,"w")
        for client in clienti:
            stringDeAdaugat = client.getId() + ',' + client.getNume() + ',' + str(client.getCnp()) + "\n"
            fisier.write(stringDeAdaugat)
        fisier.close()

    def add(self,client):    
        '''
        suprascriem functia de add din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'clienti'
        '''
        clienti = self.__citesteDinFisier()
        if client not in clienti:
            clienti.append(client)
        else:
            raise RepositoryException('Obiectul exista deja in repository')
            
        self.__scrieInFisier(clienti)
        
    def update(self,clientVechi,clientNou):
        '''
        suprascriem functia de update din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'clienti'
        '''
        clienti = self.__citesteDinFisier()
        
        try:
            clienti.remove(clientVechi)
        except RepositoryException as erori:
            raise RepositoryException(str(erori))
        try:
            clienti.append(clientNou)
        except RepositoryException as sirDeErori:
            clienti.append(clientVechi)
            raise RepositoryException(str(sirDeErori))
        
        self.__scrieInFisier(clienti)
        
    def delete(self,client):
        '''
        suprascriem functia de remove din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'clienti'
        '''
        clienti = self.__citesteDinFisier()
        if client in clienti:
            clienti.remove(client)
        else:
            raise RepositoryException('Obiectul nu exista in repository')
        
        self.__scrieInFisier(clienti)
        
    def getAll(self):
        '''
        suprascriem functia getAll din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'carti'
        '''
        return self.__citesteDinFisier()
    
    def getById(self,id):
        '''
        suprascriem functia getbyId
        '''
        clienti = self.__citesteDinFisier()
        for client in clienti:
            if client.getId() == id:
                return client
            
        raise RepositoryException("Nu s-a gasit!")

        
        
