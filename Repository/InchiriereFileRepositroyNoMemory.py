'''
Created on 9 Dec 2018

@author: Birdie
'''
from Repository.Repository import Repository
from domeniu.Client import Client
from domeniu.Carte import Carte
from domeniu.Inchiriere import Inchiriere
from Validator.Exceptii import RepositoryException

class InchiriereFileRepositoryNoMemory(Repository):
    
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
        inchirieri = []
        while linieDinFisier != "":
            cuvinte = linieDinFisier.split(',')
            carte = Carte(cuvinte[0],'nume','descriere','autor')
            client = Client(cuvinte[1],'nume','cnp')
            inchirieri.append(Inchiriere(carte,client))
            linieDinFisier = fisier.readline().strip()
        fisier.close()
        return inchirieri
    
    def __scrieInFisier(self,inchirieri):
        '''
        Incarca datele din memorie in fisier
        '''
        fisier = open(self.__nume_fisier,"w")
        for inchiriere in inchirieri:
            stringDeAdaugat = inchiriere.getCarte().getId() + ',' + inchiriere.getClient().getId() + "\n"
            fisier.write(stringDeAdaugat)
        fisier.close()

    def add(self,inchiriere):    
        '''
        suprascriem functia de add din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'inchirieri'
        '''
        inchirieri = self.__citesteDinFisier()
        if inchiriere not in inchirieri:
            inchirieri.append(inchiriere)
        else:
            raise RepositoryException('Obiectul exista deja in repository')
            
        self.__scrieInFisier(inchirieri)
        
        
    def delete(self,inchiriere):
        '''
        suprascriem functia de remove din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'inchirieri'
        '''
        inchirieri = self.__citesteDinFisier()
        if inchiriere in inchirieri:
            inchirieri.remove(inchiriere)
        else:
            raise RepositoryException('Obiectul nu exista in repository')
        
        self.__scrieInFisier(inchirieri)
        
    def getAll(self):
        '''
        suprascriem functia getAll din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'carti'
        '''
        return self.__citesteDinFisier()

        
        
