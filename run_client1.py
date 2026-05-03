from client import *
from dbclient import *
from constRPC import *
from time import sleep

if __name__ == "__main__":
    print("Iniciando Cliente 1...")
    c1 = Client(PORTC1)                # create client
    dbC1 = DBClient(HOSTS, PORTS)      # create reference
    
    print(f"Conectando ao Servidor em {HOSTS}:{PORTS}...")
    dbC1.create()                      # create new list
    dbC1.appendData('Client 1')        # append some data
    
    print("Lista criada e 'Client 1' inserido.")
    print("Aguardando 5 segundos para garantir que o Cliente 2 esteja aguardando...")
    sleep(5)
    
    print(f"Enviando referencia (stub) para Cliente 2 no IP {HOSTC2}:{PORTC2}...")
    c1.sendTo(HOSTC2, PORTC2, dbC1)    # send to other client
    print("Enviado com sucesso. Cliente 1 finalizando.")
