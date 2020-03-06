'''
Created on 19 Nov 2018

@author: Birdie
'''
from Validator.Exceptii import ValidationException

class Validator:
    
    @staticmethod
    def valideazaCarte(carte):
        
        '''
        Functie care valideaza carte
        '''
        
        erori = ""

        if int(carte.getId()) < 0:
            erori += "id trebuie sa fie pozitiv\n"
        if carte.getDescriere() == '':
            erori += "Cartea nu poate avea descriere vida\n"
        if carte.getTitlu() == '':
            erori += "Titlul nu poate fi vid\n"
        if carte.getAutor() == '':
            erori += "Autorul nu poate avea nume vid\n"
            
        if len(erori) > 0:
            raise ValidationException(erori)
        
    @staticmethod
    def valideazaClient(client):
        
        '''
        Functie care valideaza client
        '''
        
        erori = ""
        
        if int(client.getId()) < 0:
            erori += "id trebuie sa fie pozitiv\n"
        if client.getNume() == '':
            erori += "nume vid\n"
        if int(client.getCnp()) < 0 or int(client.getCnp()) > 100000000000000 or int(client.getCnp()) <= 999999999999:
            erori += "CNP-ul trebuie sa fie un numar pozitiv de 13 cifre\n"
            
        if len(erori) > 0:
            raise ValidationException(erori)