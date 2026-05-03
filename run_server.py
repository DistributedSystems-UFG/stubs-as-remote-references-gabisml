from server import *
from constRPC import *

if __name__ == "__main__":
    print("Iniciando Servidor na porta", PORTS, "...")
    server = Server(PORTS)
    server.run()
