'''
Created on 9 Dec 2018

@author: Birdie
'''
from Repository.Repository import Repository
from domeniu.Client import Client

class ClientFisierRepository(Repository):
    
    def __init__(self,nume_fisier):
        Repository.__init__(self)
        self.__nume_fisier = nume_fisier
        self.__citesteDinFisier()
        
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
    
    def __scrieInFisier(self):
        '''
        Incarca datele din memorie in fisier
        '''
        fisier = open(self.__nume_fisier,"w")
        clienti = Repository.getAll(self)
        for client in clienti:
            stringDeAdaugat = client.getId() + ',' + client.getNume() + ',' + client.getCnp() + "\n"
            fisier.write(stringDeAdaugat)
        fisier.close()

    def add(self,client):    
        '''
        Functie mostenita add la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.add(self,client)
        self.__scrieInFisier()
        
    def update(self,clientVechi,clientNou):
        '''
        Functie mostenita update la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.update(self,clientVechi,clientNou)
        self.__scrieInFisier()
        
    def delete(self,client):
        '''
        Functie mostenita sterge la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.delete(self,client)
        self.__scrieInFisier()
        
        
