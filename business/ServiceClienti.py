'''
Created on 19 Nov 2018

@author: Birdie
'''
from Validator.Exceptii import *
from Validator.Validators import *
from domeniu.Client import *
import string
import random

class ServiceClienti:   
    
    def __init__(self, repositoryClienti):
        self.__repositoryClienti = repositoryClienti
        
    def adaugaClient(self, ID, nume, cnp):
        '''
        Functie care valideaza datele clientului dat si apoi il adauga in baza de date
        '''
        client = Client(ID, nume, cnp)
        Validator.valideazaClient(client)
        self.__repositoryClienti.add(client)
        
    def stergeClient(self, ID):
        '''
        Functie care valideaza datele unui client si apoi il sterge din baza de date(daca exista)
        '''
        client = self.__repositoryClienti.getById(ID)
        Validator.valideazaClient(client)
        self.__repositoryClienti.remove(client)
        
    def modificaClient(self,ID,numeNou,cnpNou):
        '''
        Functie care modifica un client
        '''
        clientVechi = self.__repositoryClienti.getById(ID)
        clientNou = Client(ID,numeNou,cnpNou)
        Validator.valideazaClient(clientVechi)
        Validator.valideazaClient(clientNou)
        self.__repositoryClienti.update(clientVechi, clientNou)
    
    def listaClienti(self):
        '''
        Functie care creeaza lista de clienti
        '''
        clienti = self.__repositoryClienti.getAll()
        listaClienti = []
        for element in clienti:
            listaClienti.append(str(element))
        return listaClienti
    
    @staticmethod
    def randomstring(lungime):
        litere = string.ascii_lowercase
        return ''.join(random.choice(litere) for i in range(lungime))
    
    @staticmethod
    def randomnumber(lungime):
        numere = "123456789"
        return ''.join(random.choice(numere) for i in range(lungime))
    
    def randomClienti(self,numarDeAdaugari):
        '''
        Metoda care adauga la repository clienti de un numar dat de ori
        '''
        for i in range(0,numarDeAdaugari):
            ID = self.randomnumber(2)
            nume = self.randomstring(6)
            cnp = self.randomnumber(13)
            self.adaugaClient(ID,nume,cnp)
            
    def getAllClienti(self):
        listaDeClienti = self.__repositoryClienti.getAll()
        return listaDeClienti
            
    def cautareClient(self, stringDeCautat):
        '''
        Functie care cauta o carte in baza de date
        '''
        listaDeAfisat = []
        listaDeClienti = ServiceClienti.getAllClienti(self)
        for client in listaDeClienti:
            if stringDeCautat in client.getNume():
                listaDeAfisat.append(client)
        if len(listaDeAfisat) == 0:
            raise ValidationException('nu s-a gasit')
        else:
            return listaDeAfisat