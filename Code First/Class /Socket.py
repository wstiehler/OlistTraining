import socket

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((HOST , PORT)) #bind = Subir o server no host e na porta especifica
    s.listen()
    coon , addr = s.accept()

    with coon:
        print("Dados do cliente:" , addr)
        while True:
            data = coon.recv(1024)
            if not data:
                break
        coon.sendall(data) #sendall ele pode mandar qualquer tamanho de dados.