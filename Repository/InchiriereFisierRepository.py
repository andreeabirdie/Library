'''
Created on 9 Dec 2018

@author: Birdie
'''
from Repository.Repository import Repository
from domeniu.Inchiriere import Inchiriere
from domeniu.Carte import Carte
from domeniu.Client import Client

class InchiriereFisierRepository(Repository):
    
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
        inchirieri = []
        while linieDinFisier != "":
            cuvinte = linieDinFisier.split(',')
            carte = Carte(cuvinte[0],'nume','descriere','autor')
            client = Client(cuvinte[1],'nume','cnp')
            inchirieri.append(Inchiriere(carte,client))
            linieDinFisier = fisier.readline().strip()
        fisier.close()
        return inchirieri
    
    def __scrieInFisier(self):
        '''
        Incarca datele din memorie in fisier
        '''
        fisier = open(self.__nume_fisier,"w")
        inchirieri = Repository.getAll(self)
        for inchiriere in inchirieri:
            stringDeAdaugat = inchiriere.getCarte().getId() + ',' + inchiriere.getClient().getId() + "\n"
            fisier.write(stringDeAdaugat)
        fisier.close()

    def add(self,inchiriere):    
        '''
        Functie mostenita add la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.add(self,inchiriere)
        self.__scrieInFisier()

        
    def delete(self,inchiriere):
        '''
        Functie mostenita sterge la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.delete(self,inchiriere)
        self.__scrieInFisier()
        
        
