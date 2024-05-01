import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(5)
client_socket, client_address = server_socket.accept()

while True:
    send_data = input("Digite a mensagem para enviar ao cliente: ").encode("utf-8")
    client_socket.send(send_data)
    if send_data == b"vlw cpc":
        break
    
    received_data = client_socket.recv(1024)
    print("Dados recebidos do cliente:", received_data.decode("utf-8"))
    
client_socket.close()