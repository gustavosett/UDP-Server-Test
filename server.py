import socket

def udp_server():
    # Criar um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Vincular o socket a um endereço e porta
    server_address = ('localhost', 10000)
    sock.bind(server_address)

    while True:
        print("\nServidor UDP aguardando mensagens...")
        data, address = sock.recvfrom(4096)

        if data:
            print("Recebido: ", data.decode())
            sent = sock.sendto(data, address)
            print("Enviado ", sent, " bytes de volta para ", address)

# Executar o servidor
udp_server()
