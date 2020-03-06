'''
Created on 19 Nov 2018

@author: Birdie
'''
from Validator.Exceptii import *
import copy

class Repository:
    
    def __init__(self):
        self.__repository = []
        
    def add(self, obiect):
        '''
        Metoda care adauga un element in baza de date
        '''
        if obiect not in self.__repository:
            self.__repository.append(obiect)
        else:
            raise RepositoryException('Obiectul exista deja in repository')
        
    def delete(self, obiect):
        '''
        Metoda care sterge un element din baza de date
        '''
        if obiect in self.__repository:
            self.__repository.remove(obiect)
        else:
            raise RepositoryException('Obiectul nu exista in repository')
        
    def update(self, obiectVechi, obiectNou):
        '''
        Metoda care updateaza un element din baza de date
        '''
        try:
            self.delete(obiectVechi)
        except RepositoryException as erori:
            raise RepositoryException(str(erori))
        try:
            self.add(obiectNou)
        except RepositoryException as sirDeErori:
            self.add(obiectVechi)
            raise RepositoryException(str(sirDeErori))
        
    def find(self, obiect):
        '''
        Metoda care cauta un element in baza de date
        '''
        if obiect in self.__repository:
            return True
        return False
    
    def getById(self,id):
        '''
        metoda care cauta un obiect in repository dupa id
        '''
        for obiect in self.__repository:
            if obiect.getId() == id:
                return obiect
            
        raise RepositoryException("Nu s-a gasit!")
            
    def getAll(self):
        '''
        Metoda care returneaza continutul bazei de date
        '''
        return copy.deepcopy(self.__repository)
    
    '''
    def getAllElements(self):
        return self.__repository[:]
    '''
            