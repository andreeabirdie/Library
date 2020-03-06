'''
Created on 16 Dec 2018

@author: Birdie
'''
import unittest
from domeniu.Carte import Carte
from Validator.Validators import Validator
from business.ServiceClienti import ServiceClienti
from business.ServiceCarti import ServiceCarti
from Repository.Repository import Repository
from Validator.Exceptii import ValidationException, RepositoryException
from domeniu.Client import Client


class TestCarti(unittest.TestCase):


    def setUp(self):
        self.carteCorecta = Carte(32,'Enigma Otiliei','blah','George Calinescu')
        self.carteGresita = Carte(-65,'','','')
        self.aceeasiCarte = Carte(32,'Ion','pamant','Liviu Rebreanu')

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testGetId(self):
        self.assertEqual(self.carteCorecta.getId(), 32)
        
    def testDublura(self):
        self.assertTrue(self.carteCorecta == self.aceeasiCarte)
        
        
class TestClienti(unittest.TestCase):   
    
    def setUp(self):
        self.carteCorecta = Carte(32,'Enigma Otiliei','blah','George Calinescu')
        self.aceeasiCarte = Carte(32,'Ion','pamant','Liviu Rebreanu')

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testGetId(self):
        self.assertEqual(self.carteCorecta.getId(), 32)
        
    def testDublura(self):
        self.assertTrue(self.carteCorecta == self.aceeasiCarte)
        
class TestServiceSiRepositoryCarte(unittest.TestCase):
    
    def setUp(self):
        self.repositoryCarti = Repository()
        self.serviceCarte = ServiceCarti(self.repositoryCarti)
        self.validator = Validator()
        

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testServiceCarti(self):
        self.assertRaises(ValidationException,self.serviceCarte.adaugaCarte,-2, '', '', '')
        carteCorecta = Carte(2,'poezii','filosofie','eu')
        self.repositoryCarti.add(carteCorecta)
        self.assertRaises(RepositoryException,self.repositoryCarti.add,carteCorecta)
        self.repositoryCarti.delete(carteCorecta)
        self.assertRaises(RepositoryException,self.repositoryCarti.delete,carteCorecta)
        self.assertRaises(RepositoryException,self.repositoryCarti.update,carteCorecta,carteCorecta)
        
class TestServiceSiRepositoryClient(unittest.TestCase):
    
    def setUp(self):
        self.repositoryClient = Repository()
        self.serviceClient = ServiceClienti(self.repositoryClient)
        self.validator = Validator()
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testServiceCarti(self):
        self.assertRaises(ValidationException,self.serviceClient.adaugaClient,-2, '', 22)
        clientCorect = Client(12,'Ana',6666666666666)
        self.repositoryClient.add(clientCorect)
        self.assertRaises(RepositoryException,self.repositoryClient.add,clientCorect)
        self.repositoryClient.delete(clientCorect)
        self.assertRaises(RepositoryException,self.repositoryClient.delete,clientCorect)
        self.assertRaises(RepositoryException,self.repositoryClient.update,clientCorect,clientCorect)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()