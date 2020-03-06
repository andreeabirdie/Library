from business.ServiceCarti import ServiceCarti
from business.ServiceClienti import ServiceClienti
from Repository.Repository import Repository
from console.Console import Console
from teste.Teste import Test
from business.ServiceInchiriere import ServiceInchiriere
from Repository.CarteFisierRepository import CarteFisierRepository
from Repository.ClientFisierRepository import ClientFisierRepository
from Repository.InchiriereFisierRepository import InchiriereFisierRepository
from Repository.CarteFileRepositoryNoMemory import CarteFileRepositoryNoMemory
from Repository.ClientFileRepositoryNoMemory import ClientFileRepositoryNoMemory
from Repository.InchiriereFileRepositroyNoMemory import InchiriereFileRepositoryNoMemory

def __main__():
    
    testeleProgramului = Test()
    testeleProgramului.runtests()
    
    #in memory
    '''
    cartiRepository = Repository()
    clientiRepository = Repository()
    inchiriereRepository = Repository()
    '''
    
    #file repository
    '''
    cartiRepository = CarteFisierRepository('carti.txt')
    clientiRepository = ClientFisierRepository('clienti.txt')
    inchiriereRepository = InchiriereFisierRepository('inchirieri.txt')
    '''
    
    #file repository no memory
    cartiRepository = CarteFileRepositoryNoMemory('carti.txt')
    clientiRepository = ClientFileRepositoryNoMemory('clienti.txt')
    inchiriereRepository = InchiriereFileRepositoryNoMemory('inchirieri.txt')
    
    
    serviceCarti = ServiceCarti(cartiRepository)
    serviceClienti = ServiceClienti(clientiRepository)
    serviceInchiriere = ServiceInchiriere(cartiRepository,clientiRepository,inchiriereRepository)
    ui = Console(serviceCarti,serviceClienti,serviceInchiriere)
    Console.meniu(ui)
    

__main__()