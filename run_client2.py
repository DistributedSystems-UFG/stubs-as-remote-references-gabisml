import pickle
from client import *
from dbclient import *
from constRPC import *

if __name__ == "__main__":
    print("Iniciando Cliente 2 na porta", PORTC2, "...")
    c2 = Client(PORTC2)                # create a new client
    
    print("Aguardando recebimento da referencia do Cliente 1...")
    data = c2.recvAny()                # block until data is sent
    dbC2 = pickle.loads(data)          # receive reference
    
    print("Referencia recebida! Inserindo 'Client 2' na lista do servidor...")
    dbC2.appendData('Client 2')        # append data to same list
    
    print("Buscando lista atualizada do servidor:")
    print(dbC2.getValue())
    
    print("Enviando sinal de STOP para o servidor...")
    c2.sendTo(HOSTS, PORTS, [STOP])
    print("Cliente 2 finalizando.")
