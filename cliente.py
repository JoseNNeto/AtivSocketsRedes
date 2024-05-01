import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

while True:
    received_data = client_socket.recv(1024)
    print("Dados recebidos do servidor:", received_data.decode("utf-8"))
    
    send_data = input("Digite a mensagem para enviar ao servidor: ").encode("utf-8")
    client_socket.send(send_data)
    if send_data == b"vlw cpc":
        break

client_socket.close()