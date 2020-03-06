'''
Created on 9 Dec 2018

@author: Birdie
'''
from Repository.Repository import Repository
from domeniu.Carte import Carte

class CarteFisierRepository(Repository):
    
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
        carti = []
        while linieDinFisier != "":
            cuvinte = linieDinFisier.split(',')
            carti.append(Carte(cuvinte[0],cuvinte[1],cuvinte[2],cuvinte[3]))
            linieDinFisier = fisier.readline().strip()
        fisier.close()
        return carti
    
    def __scrieInFisier(self):
        '''
        Incarca datele din memorie in fisier
        '''
        fisier = open(self.__nume_fisier,"w")
        carti = Repository.getAll(self)
        for carte in carti:
            stringDeAdaugat = carte.getId() + ',' + carte.getTitlu() + ',' + carte.getDescriere() + ',' + carte.getAutor() + "\n"
            fisier.write(stringDeAdaugat)
        fisier.close()

    def add(self,carte):    
        '''
        Functie mostenita add la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.add(self,carte)
        self.__scrieInFisier()
        
    def update(self,carteVeche,carteNoua):
        '''
        Functie mostenita update la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.update(self,carteVeche,carteNoua)
        self.__scrieInFisier()
        
    def delete(self,carte):
        '''
        Functie mostenita sterge la care adaugam citirea si scrierea din/in fisier
        '''
        Repository.delete(self,carte)
        self.__scrieInFisier()
        
        
