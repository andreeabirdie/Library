'''
Created on 19 Nov 2018

@author: Birdie
'''
from Validator.Exceptii import *
from Validator.Validators import *
from Repository.Repository import Repository
from business.ServiceCarti import ServiceCarti
from business.ServiceClienti import ServiceClienti
from domeniu.Carte import *
from domeniu.Client import *
from business.ServiceInchiriere import ServiceInchiriere
from domeniu.Inchiriere import Inchiriere


class Test():
    
    def __init__(self):
        self.__idCorect = 125
        self.__titluCorect = "Ion"
        self.__descriereCorecta = "pamant"
        self.__autorCorect = "Liviu Rebreanu"
        self.__carteCorecta = Carte(self.__idCorect,self.__titluCorect,self.__descriereCorecta,self.__autorCorect)
        
        self.__idGresit = -56
        self.__titluGresit = ""
        self.__descriereGresita = ""
        self.__autorGresit = ""
        self.__carteGresita = Carte(self.__idGresit,self.__titluGresit,self.__descriereGresita,self.__autorGresit)
        
        self.__idclientCorect = 456
        self.__numeCorect = "eu"
        self.__cnpCorect = "2111111111111"
        self.__clientCorect = Client(self.__idclientCorect,self.__numeCorect,self.__cnpCorect)
        
        self.__idclientGresit = -98
        self.__numeGresit = ""
        self.__cnpGresit = 12225
        self.__clientGresit = Client(self.__idclientGresit,self.__numeGresit,self.__cnpGresit)
        
        self.__inchiriereCorecta = Inchiriere(self.__carteCorecta,self.__clientCorect)
        
        self.__repositoryCarti = Repository()
        self.__repositoryClienti = Repository()
        self.__serviceCarti = ServiceCarti(self.__repositoryCarti)
        self.__serviceClienti = ServiceClienti(self.__repositoryClienti)
        
        self.__repositoryInchiriere = Repository()
        self.__serviceInchiriere = ServiceInchiriere(self.__repositoryCarti,self.__repositoryClienti,self.__repositoryInchiriere)
        
    def __testCarte(self):
        assert self.__idCorect == self.__carteCorecta.getId()
        assert self.__titluCorect == self.__carteCorecta.getTitlu()
        assert self.__descriereCorecta == self.__carteCorecta.getDescriere()
        assert self.__autorCorect == self.__carteCorecta.getAutor()
        
    def __testClient(self):
        assert self.__idclientCorect == self.__clientCorect.getId()
        assert self.__numeCorect == self.__clientCorect.getNume()
        assert self.__cnpCorect == self.__clientCorect.getCnp()
    
    def __testInchiriere(self):
        assert self.__carteCorecta == self.__inchiriereCorecta.getCarte()
        assert self.__clientCorect == self.__inchiriereCorecta.getClient()
        
    def __testValideazaCarte(self):
        try:
            Validator.valideazaCarte(self.__carteCorecta)
        except ValidationException:
            assert False
            
        try:
            Validator.valideazaCarte(self.__carteGresita)
            assert False
        except ValidationException as sirDeErori:
            assert str(sirDeErori) == "id trebuie sa fie pozitiv\nCartea nu poate avea descriere vida\nTitlul nu poate fi vid\nAutorul nu poate avea nume vid\n" 
        
    def __testValideazaClient(self):
        try:
            Validator.valideazaClient(self.__clientCorect)
        except ValidationException:
            assert False
            
        try:
            Validator.valideazaClient(self.__clientGresit)
            assert False
        except ValidationException as sirDeErori:
            assert str(sirDeErori) == "id trebuie sa fie pozitiv\nnume vid\nCNP-ul trebuie sa fie un numar pozitiv de 13 cifre\n" 
            
    def __testRepositoryCarti(self):
        self.__repositoryCarti.add(self.__carteCorecta)
        lista = []
        lista.append(self.__carteCorecta)
        
        assert self.__repositoryCarti.getAll() == lista
        
        self.__repositoryCarti.delete(self.__carteCorecta)
        
        assert self.__repositoryCarti.getAll() == []
        
        
    def __testRepositoryClienti(self):
        self.__repositoryClienti.add(self.__clientCorect)
        lista = []
        lista.append(self.__clientCorect)
        
        assert self.__repositoryClienti.getAll() == lista
        
        self.__repositoryClienti.delete(self.__clientCorect)
        
        assert self.__repositoryClienti.getAll() == []
        
    def __testCautaCarte(self):
        self.__repositoryCarti.add(self.__carteCorecta)
        assert self.__serviceCarti.cautareCarte('Io') == [Carte(125, 'Ion', 'Liviu Rebreanu', 'pamant')]
        
    def __testCautaClient(self):
        self.__repositoryClienti.add(self.__clientCorect)
        assert self.__serviceClienti.cautareClient('e') == [Client(456, 'eu', '2111111111111')]
        
    def __testRepositoryInchiriere(self):
        self.__repositoryInchiriere.add(self.__inchiriereCorecta)
        lista = []
        lista.append(self.__inchiriereCorecta)
        
        assert self.__repositoryInchiriere.getAll() == lista
        
    def __testStergeCarte(self):
        self.__repositoryClienti.add(self.__clientCorect)
        self.__repositoryCarti.add(self.__carteCorecta)
        self.__repositoryInchiriere.add(self.__inchiriereCorecta)
        
    def __testModificaCarte(self):
        self.__serviceCarti.modificaCarte(125,'Enigma Otiliei', 'misterul feminin', 'George Calinescu')
        
        assert self.__repositoryCarti.getAll() == [(Carte(125,'Enigma Otiliei', 'misterul feminin', 'George Calinescu'))]
        
    def __testModificaClient(self):
        self.__serviceClienti.modificaClient(456,'Oana Vrabie',2222222222222)
        
        assert self.__repositoryClienti.getAll() == [Client(456,'Oana Vrabie',2222222222222)]
        
    def __testserviceCarti(self):
        assert self.__serviceCarti.listaCarti() == ['id: 125 titlu: Enigma Otiliei autor: George Calinescu descriere: misterul feminin']
        
        self.__serviceCarti.adaugaCarte(45,'Ion','pamant','Liviu Rebreanu')
        
        assert self.__serviceCarti.listaCarti() == ['id: 125 titlu: Enigma Otiliei autor: George Calinescu descriere: misterul feminin', 'id: 45 titlu: Ion autor: Liviu Rebreanu descriere: pamant']
    
    
    def __testserviceClienti(self):
        assert self.__serviceClienti.listaClienti() == ['id: 456 nume: Oana Vrabie cnp: 2222222222222']
        
        self.__serviceClienti.adaugaClient(1,'Andreea Vrabie',1111111111111)

        assert self.__serviceClienti.listaClienti() == ['id: 456 nume: Oana Vrabie cnp: 2222222222222', 'id: 1 nume: Andreea Vrabie cnp: 1111111111111']              
                                        
    def __testlistaInchirieri(self):
        assert self.__serviceInchiriere.listaInchiriere() == ['Cartea cu id: 125 a fost inchiriata de clientul cu id: 456'] 
        
    def __testRaport1(self):
        self.__serviceCarti.adaugaCarte(7, 'Poveste', 'povesti minunate', 'autor minunat')
        self.__serviceInchiriere.adaugaInchiriere(7, 456)
        self.__serviceInchiriere.stergeInchiriere(7, 456)
        self.__serviceInchiriere.adaugaInchiriere(7, 456)
        self.__serviceCarti.adaugaCarte(8, 'Super poezii', 'life is art man', 'Super autor')
        self.__serviceInchiriere.adaugaInchiriere(8, 1)
        
        assert self.__serviceInchiriere.CeaMaiInchiriata() == [7]
        
        self.__serviceInchiriere.stergeInchiriere(8, 1)
        self.__serviceInchiriere.adaugaInchiriere(8, 1)
        
        assert self.__serviceInchiriere.CeaMaiInchiriata() == [7,8]
        
    def __testRaport2(self):
        assert self.__serviceInchiriere.chiriasiOrdonatiNume() == [[1,'Andreea Vrabie'], [456,'Oana Vrabie']]
    
    def __testRaport3(self):
        assert self.__serviceInchiriere.chiriasiOrdonatiNumar() == [[1, 1], [456, 2]]
    
    def __testRaport4(self):
        assert self.__serviceInchiriere.CeiMaiActivi() == [[456,2]]
    
    def __testRaport5(self):
        assert self.__serviceInchiriere.CartiInchirirateOrdonateDupaNume() == ['Enigma Otiliei', 'Poveste', 'Super poezii']
    
    def runtests(self):
        self.__testCarte()
        self.__testClient()
        self.__testValideazaCarte()
        self.__testValideazaClient()
        self.__testRepositoryCarti()
        self.__testRepositoryClienti()
        self.__testCautaCarte()
        self.__testCautaClient()
        self.__testRepositoryInchiriere()
        self.__testModificaCarte()
        self.__testModificaClient()
        self.__testInchiriere()
        self.__testserviceCarti()
        self.__testserviceClienti()
        self.__testlistaInchirieri()
        self.__testRaport1()
        self.__testRaport2()
        self.__testRaport3()
        self.__testRaport4()
        self.__testRaport5()