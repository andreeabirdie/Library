'''
Created on 19 Nov 2018

@author: Birdie
'''
from business.ServiceInchiriere import ServiceInchiriere
from domeniu.Carte import Carte
class Console:
    
    def __init__(self, serviceCarti, serviceClienti, ServiceInchiriere):
        self.__serviceInchiriere = ServiceInchiriere
        self.__serviceCarti = serviceCarti
        self.__serviceClienti = serviceClienti
        
    '''
    @staticmethod
    def valideazaInt(numar):
        try:
            numar = int(numar)
        except ValueError:
            return None
        return numar
    '''

    def meniu(self):
        #self.__printMenu()
        while True:
            print('\n1. Adauga')
            print("\t",'a. Adauga carte')
            print("\t",'b. Adauga client')
            print("\t",'c. Adauga carti aleator')
            print("\t",'d. Adauga clienti aleator')
            print("\t",'e. Inchiriaza carte')
            
            print('2. Sterge')
            print("\t",'a. Sterge carte')
            print("\t",'b. Sterge client')
            print("\t",'c. Returneaza carte')
            
            print('3.Modifica')
            print("\t",'a. Modifica carte')
            print("\t",'b. Modifica client')
            
            print('4.Afiseaza')
            print("\t",'a. Lista carti')
            print("\t",'b. Lista clienti')
            print("\t",'c. Lista de inchirieri')
    
            print('5.Cauta')
            print("\t",'a. Cauta carte')
            print("\t",'b. Cauta client')
            
            print('6.Rapoarte')
            print("\t",'a. Cele mai inchiriate carti')
            print("\t",'b. Clienti cu carti inchiriate ordonati dupa nume')
            print("\t",'c. Clienti cu carti inchiriate ordonati dupa numarul de carti inchiriate')
            print("\t",'d. Primii 20% cei mai activi clienti')
            print("\t",'e. Carti inchiriate ordonate dupa nume')
    
            print()
            
            command = input("introduceti o comanda:")
            
            if (command == '1a'):
                #ID, titlu, descriere, autor
                ID = input('\nid: ')
                titlu = input('titlu: ')
                descriere = input('descriere: ')
                autor = input('autor: ') 
                try:
                    self.__serviceCarti.adaugaCarte(ID, titlu, descriere, autor)
                    print('\n____Cartea a fost adaugata cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '1b'):
                #ID, nume, cnp
                ID = input('\nid: ')
                nume = input('nume: ')
                cnp = input('cnp: ')
                try:
                    self.__serviceClienti.adaugaClient(ID, nume, cnp)
                    print('\n____Clientul a fost adaugat cu succes!___')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
            
            elif (command == '1c'):
                numarDeAdaugari = int(input('\nCate carti doriti sa adaugati? \n >>'))
                try:
                    self.__serviceCarti.randomCarti(numarDeAdaugari)
                    print('\n____Cartile corecte au fost adaugate cu succes!___')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '1d'):
                numarDeAdaugari = int(input('\nCati clienti doriti sa adaugati? \n >>'))
                try:
                    self.__serviceClienti.randomClienti(numarDeAdaugari)
                    print('\n____Clientii corecti au fost adaugati cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '1e'):
                idCarte = input('\nid-ul cartii: ')
                idClient = input('id-ul clientului: ')
                try:
                    self.__serviceInchiriere.adaugaInchiriere(idCarte,idClient)
                    print('\n____Imprumutul a fost realizat cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '2a'):
                ID = input('id: ') 
                try:
                    self.__serviceInchiriere.stergeCarte(ID)
                    print('\n____Cartea si toate imprumuturile ei au fost sterse cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '2b'):
                ID = input('id: ') 
                try:
                    self.__serviceInchiriere.stergeClient(ID)
                    print('\n____Clientul si toate imprumuturile lui au fost sterse cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                
            elif (command == '2c'):
                idcarte = input('\nid-ul cartii inchiriate')
                idclient = input('id-ul chiriasului')  
                try: 
                    self.__serviceInchiriere.stergeInchiriere(idcarte,idclient) 
                    print('\n____Imprumutul a fost sters cu succes!____')
                except Exception as sirDeErori:  
                    print(str(sirDeErori)) 
                    
            elif (command == '3a'):
                ID = input('\nidul cartii de modificat: ')
                titluNou = input('noul titlu: ')
                descriereNoua = input('noua descriere: ')
                autorNou = input('noul autor: ')
                try:
                    self.__serviceCarti.modificaCarte(ID,titluNou,descriereNoua,autorNou)
                    print('\n___Cartea a fost modificata cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))   
                
            elif (command == '3b'):
                ID = input('idul clientului de modificat: ')
                numeNou = input('noul nume: ')
                cnpNou = input('noul cnp: ')
                try:
                    self.__serviceClienti.modificaClient(ID,numeNou,cnpNou)
                    print('\n___Clientul a fost modificat cu succes!____')
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '4a'):
                listaCarti = self.__serviceCarti.listaCartiRecursiv()
                print('\n')
                for carte in listaCarti:
                    print(carte)
                
            elif (command == '4b'):
                print('\n')
                listaClienti = self.__serviceClienti.listaClienti()
                for client in listaClienti:
                    print(client)
            
            elif (command == '4c'):
                print('\n')
                listaInchiriere = self.__serviceInchiriere.listaInchiriere()
                for inchiriere in listaInchiriere:
                    print(inchiriere)
                    
            elif (command == '5a'):
                stringDeCautat = input('\n Ce doriti sa cautati? \n >>')
                try: 
                    print('\n')
                    for carte in self.__serviceCarti.cautareCarteRecursiv(stringDeCautat):
                        print(carte)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '5b'):
                stringDeCautat = input('\n Ce doriti sa cautati? \n >>')
                try: 
                    print('\n')
                    for client in self.__serviceClienti.cautareClient(stringDeCautat):
                            print(client)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '6a'):
                try:
                    listaCarti = self.__serviceInchiriere.CeaMaiInchiriata()
                    print('\n Cartile cele mai inchiriate sunt cartile cu id:')
                    for element in listaCarti:
                        print(element)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                
            elif (command == '6b'):
                try:
                    print('\n')
                    listaClienti = self.__serviceInchiriere.chiriasiOrdonatiNume()
                    for element in listaClienti:
                        print(element)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '6c'):
                try:
                    print('\n')
                    listaClienti = self.__serviceInchiriere.chiriasiOrdonatiNumar()
                    for element in listaClienti:
                        print(element)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '6d'):
                try:
                    print('\n')
                    listaClienti = self.__serviceInchiriere.CeiMaiActivi()
                    for element in listaClienti:
                        print(element)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                    
            elif (command == '6e'):
                try:
                    print('\n')
                    listaCarti = self.__serviceInchiriere.CartiInchirirateOrdonateDupaNume()
                    for element in listaCarti:
                        print(element)
                except Exception as sirDeErori:
                    print(str(sirDeErori))
                
            elif (command == '0'):
                return False
    
            else: 
                print('comanda invalida!')