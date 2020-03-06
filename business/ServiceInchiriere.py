from domeniu.Inchiriere import *
from Validator.Validators import Validator
from _operator import itemgetter
from Validator.Exceptii import ValidationException
from utils import SelectionSort, ShakerSort

class ServiceInchiriere:
    
    def __init__(self, cartiRepository, clientiRepository, inchiriereRepository):
        self.__repositoryCarti = cartiRepository
        self.__repositoryClienti = clientiRepository
        self.__repositoryInchiriere = inchiriereRepository
        self.__istoric = [0]*100
        
    def adaugaInchiriere(self, idcarte, idclient):
        '''
        Functie care adauga o inchiriere
        '''
        carte = self.__repositoryCarti.getById(idcarte)
        client = self.__repositoryClienti.getById(idclient)
        for imprumut in self.__repositoryInchiriere.getAll():
            carteExistenta = imprumut.getCarte()
            if carte == carteExistenta:
                raise ValidationException('Cartea a fost deja inchiriata')
                return
        inchiriere = Inchiriere(carte,client)
        self.__repositoryInchiriere.add(inchiriere)
        ServiceInchiriere.adaugaLaIstoric(self,idcarte)
        
    def adaugaLaIstoric(self,idcarte):
        '''
        Functie care contorizeaza de cate ori a fost inchiriata o carte
        '''
        idcarte = int(idcarte)
        self.__istoric[idcarte] +=1
        
    def stergeDinIstoric(self,idcarte):
        '''
        Functie care sterge din istoric o carte care nu mai exista in repository
        '''
        idcarte = int(idcarte)
        self.__istoric[idcarte] = 0
        
    def stergeInchiriere(self,idcarte,idclient):
        '''
        Functie care sterge o inchiriere
        '''
        carte = self.__repositoryCarti.getById(idcarte)
        client = self.__repositoryClienti.getById(idclient)
        Validator.valideazaCarte(carte)
        Validator.valideazaClient(client)
        inchiriere = Inchiriere(carte,client)
        self.__repositoryInchiriere.delete(inchiriere)    
        
    def listaInchiriere(self):
        '''
        Functie care creeaza lista de inchirieri
        '''
        listaInchirieri = []
        for element in self.__repositoryInchiriere.getAll():
            listaInchirieri.append(str(element))
        return listaInchirieri
        
    def stergeCarte(self, idCarte):
        '''
        Functie care sterge cartea si toate inchiriierile in care apare aceasta
        '''
        carte = self.__repositoryCarti.getById(idCarte)
        listaDeInchirieri = self.__repositoryInchiriere.getAll()
        for element in listaDeInchirieri:
            if element.getCarte() == carte:
                self.__repositoryInchiriere.delete(element)
        self.__repositoryCarti.delete(carte)
        
        ServiceInchiriere.stergeDinIstoric(self, idCarte)
        
    def stergeClient(self, idClient):
        '''
        Functie care sterge cclientul si toate inchiriierile in care apare acesta
        '''
        client = self.__repositoryClienti.getById(idClient)
        listaDeInchirieri = self.__repositoryInchiriere.getAll()
        for element in listaDeInchirieri:
            if element.getClient() == client:
                self.__repositoryInchiriere.delete(element)
        self.__repositoryClienti.delete(client)
     
 
    def CeaMaiInchiriata(self):
        '''
        Functie care determina lista cu id-urile cartilor cele mai inchiriate din istoric
        '''
        maxim = 0
        listaDeAfisat = []
        for i in range(0,100):
            if self.__istoric[i] > maxim:
                maxim = self.__istoric[i]
        for idcarte in range(0,len(self.__istoric)):
            if self.__istoric[idcarte] == maxim:
                listaDeAfisat.append(idcarte)
        return listaDeAfisat
            
            
    def chiriasiOrdonatiNume(self):
        '''
        Functie care ordoneaza dupa nume clientii care au imprumutat carti
        '''
        listaDeImprumuturi = self.__repositoryInchiriere.getAll()
        listaClienti = []
        for obiect in listaDeImprumuturi:
            client = obiect.getClient()
            idclient = client.getId()
            client = self.__repositoryClienti.getById(idclient)
            clientulExista = 0
            for lista in listaClienti:
                if idclient == lista[0]:
                    clientulExista = 1
            if clientulExista == 0:
                listaClienti.append([idclient,client.getNume()])
        listaClienti = SelectionSort(listaClienti, key=itemgetter(1))
        return listaClienti    
        
    def chiriasiOrdonatiNumar(self):
        '''
        Functie care ordoneaza dupa numarul de carti imprumut clientii care au imprumutat carti
        '''
        listaDeImprumuturi = self.__repositoryInchiriere.getAll()
        listaClienti = []
        for imprumut in listaDeImprumuturi:
            client = imprumut.getClient()
            idclient = client.getId()
            clientulExista = 0
            for lista in listaClienti:
                if idclient == lista[0]:
                    lista[1] +=1
                    clientulExista = 1
            if clientulExista == 0:
                listaClienti.append([idclient,1])
        listaClienti = ShakerSort(listaClienti, key=itemgetter(1))   
        return listaClienti
    
    
    def CeiMaiActivi(self):
        '''
        Functie care determina cei mai activi 20% clienti
        '''
        listaClienti = ServiceInchiriere.chiriasiOrdonatiNumar(self)
        listaClienti = ShakerSort(listaClienti, key=itemgetter(1), reverse = True)
        listaDeAfisat = []
        procentClienti = (20/100 )* len(listaClienti)
        procentClienti = int(procentClienti) +1
        for i in range(0,procentClienti):
            listaDeAfisat.append(listaClienti[i])
        return listaDeAfisat
    
    def CartiInchirirateOrdonateDupaNume(self):
        '''
        Functie care determina o lista ordonata dupa titlu a cartilor aflate in imprumut
        '''
        listaDeImprumuturi = self.__repositoryInchiriere.getAll()
        listaCarti = []
        for obiect in listaDeImprumuturi:
            carte = obiect.getCarte()
            idcarte = carte.getId()
            carte = self.__repositoryCarti.getById(idcarte)
            listaCarti.append(carte.getTitlu())
        listaCarti.sort()
        return listaCarti    