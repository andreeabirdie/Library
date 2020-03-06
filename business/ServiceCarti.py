'''
Created on 19 Nov 2018

@author: Birdie
'''
from Validator.Exceptii import *
from Validator.Validators import *
from domeniu.Carte import *
import random
import string

class ServiceCarti:
    
    def __init__(self, repositoryCarti):
        self.__repositoryCarti = repositoryCarti
        
    def adaugaCarte(self, ID, titlu, descriere, autor):
        '''
        Functie care valideaza o carte si apoi o adauga in baza de date
        '''
        carte = Carte(ID, titlu, descriere, autor)
        Validator.valideazaCarte(carte)
        self.__repositoryCarti.add(carte)
        
    def stergeCarte(self, ID):
        '''
        Functie care valideaza o carte si apoi o sterge din baza de date
        '''
        carte = self.__repositoryCarti.getById(ID)
        Validator.valideazaCarte(carte)
        self.__repositoryCarti.remove(carte)
        
    def modificaCarte(self, ID, titluNou, descriereNoua, autorNou):
        '''
        Functie care updateaza o carte daca atat cea veche cat si cea noua sunt validate
        '''
        carteVeche = self.__repositoryCarti.getById(ID)
        carteNoua = Carte(ID,titluNou,descriereNoua,autorNou)
        Validator.valideazaCarte(carteVeche)
        Validator.valideazaCarte(carteNoua)
        self.__repositoryCarti.update(carteVeche, carteNoua)

    def listaCarti(self):
        '''
        Functie care creeaza lista de carti
        '''
        carti = self.__repositoryCarti.getAll()
        listaCarti = []
        for element in carti:
            listaCarti.append(str(element))
        return listaCarti
    
    def listaCartiRecursiv(self):
        '''
        Functie care creeaza lista de carti
        '''
        carti = self.__repositoryCarti.getAll()
        listaCarti = []
        ServiceCarti.listaDeStringuri(self,carti,listaCarti,len(carti))
        return listaCarti
        
    def listaDeStringuri(self,carti,listaCarti,lungime):
        '''
        Functie care creeaza o lista de stringuri dintr-o lista de obiecte recursiv
        '''
        if lungime == 0:
            return listaCarti
        carte = str(carti[lungime-1])
        listaCarti.append(carte)
        ServiceCarti.listaDeStringuri(self, carti, listaCarti, lungime-1)
    
    @staticmethod
    def randomstring(lungime):
        litere = string.ascii_lowercase
        return ''.join(random.choice(litere) for i in range(lungime))
    
    @staticmethod
    def randomnumber(lungime):
        numere = "0123456789"
        return ''.join(random.choice(numere) for i in range(lungime))
        
    def randomCarti(self,numarDeAdaugari):
        '''
        Metoda care adauga la repository carti de un numar dat de ori
        '''
        for i in range(0,numarDeAdaugari):
            ID = self.randomnumber(2)
            titlu = self.randomstring(6)
            descriere = self.randomstring(10)
            autor = self.randomstring(3)
            self.adaugaCarte(ID,titlu,descriere,autor)
            
    def getAllCarti(self):
        listaDeCarti = self.__repositoryCarti.getAll()
        return listaDeCarti
            
    def cautareCarte(self, stringDeCautat):
        '''
        Functie care cauta o carte in baza de date
        '''
        listaDeAfisat = []
        listaDeCarti = ServiceCarti.getAllCarti(self)
        for carte in listaDeCarti:
            if stringDeCautat in carte.getTitlu():
                listaDeAfisat.append(carte)
        if len(listaDeAfisat) == 0:
            raise ValidationException('nu s-a gasit')
        else:
            return listaDeAfisat
        
    def cautareCarteRecursiv(self,stringDeCautat):
        '''
        Functie care cauta o carte in baza de date recursiv
        '''
        listaDeAfisat = []
        listaDeCarti = ServiceCarti.getAllCarti(self)
        ServiceCarti.cautaRecursiv(self,stringDeCautat,listaDeCarti,listaDeAfisat,len(listaDeCarti))
        return listaDeAfisat
        
    def cautaRecursiv(self,stringDeCautat,listaDeCarti,listaDeAfisat,lungime):
        if lungime == 0:
            return listaDeAfisat
        carte = listaDeCarti[lungime-1]
        if stringDeCautat in carte.getTitlu():
            listaDeAfisat.append(carte)
        ServiceCarti.cautaRecursiv(self,stringDeCautat,listaDeCarti,listaDeAfisat,lungime-1)