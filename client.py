import socket

def udp_client():
    # Criar um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 10000)
    message = b'Esta e a mensagem. Sera repetida.'

    try:
        # Enviar dados
        print("Enviando: ", message)
        sent = sock.sendto(message, server_address)

        # Receber resposta
        data, server = sock.recvfrom(4096)
        print("Recebido: ", data.decode())

    finally:
        print("Fechando socket")
        sock.close()

# Executar o cliente
udp_client()
