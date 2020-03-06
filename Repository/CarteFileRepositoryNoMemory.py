'''
Created on 9 Dec 2018

@author: Birdie
'''
from Repository.Repository import Repository
from domeniu.Carte import Carte
from Validator.Exceptii import RepositoryException

class CarteFileRepositoryNoMemory(Repository):
    
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
        carti = []
        while linieDinFisier != "":
            cuvinte = linieDinFisier.split(',')
            carti.append(Carte(cuvinte[0],cuvinte[1],cuvinte[2],cuvinte[3]))
            linieDinFisier = fisier.readline().strip()
        fisier.close()
        return carti
    
    def __scrieInFisier(self,carti):
        '''
        Incarca datele din memorie in fisier
        '''
        fisier = open(self.__nume_fisier,"w")
        for carte in carti:
            stringDeAdaugat = carte.getId() + ',' + carte.getTitlu() + ',' + carte.getDescriere() + ',' + carte.getAutor() + "\n"
            fisier.write(stringDeAdaugat)
        fisier.close()

    def add(self,carte):    
        '''
        suprascriem functia de add din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'carti'
        '''
        carti = self.__citesteDinFisier()
        if carte not in carti:
            carti.append(carte)
        else:
            raise RepositoryException('Obiectul exista deja in repository')
            
        self.__scrieInFisier(carti)
        
    def update(self,carteVeche,carteNoua):
        '''
        suprascriem functia de update din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'carti'
        '''
        carti = self.__citesteDinFisier()
        
        try:
            carti.remove(carteVeche)
        except RepositoryException as erori:
            raise RepositoryException(str(erori))
        try:
            carti.append(carteNoua)
        except RepositoryException as sirDeErori:
            carti.append(carteVeche)
            raise RepositoryException(str(sirDeErori))
        
        self.__scrieInFisier(carti)
        
    def delete(self,carte):
        '''
        suprascriem functia de remove din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'carti'
        '''
        carti = self.__citesteDinFisier()
        if carte in carti:
            carti.remove(carte)
        else:
            raise RepositoryException('Obiectul nu exista in repository')
        
        self.__scrieInFisier(carti)
        
    def getAll(self):
        '''
        suprascriem functia getAll din Repository general astfel incat sa nu foloseasca memoria ci doar o variabila locala 'carti'
        '''
        return self.__citesteDinFisier()
    
    def getById(self,id):
        '''
        suprascriem functia getbyId
        '''
        carti = self.__citesteDinFisier()
        for carte in carti:
            if carte.getId() == id:
                return carte
            
        raise RepositoryException("Nu s-a gasit!")

        
        
