import socket
socket_client = socket.socket()

socket_client.connect(("localhost", 6666))

while True:
    msg1 = input("please enter thr message you want to send to the server: ")

    if msg1 == 'exit':
        break

    socket_client.send(msg1.encode("UTF-8"))

    recv_data = socket_client.recv(1024)
    print(f"the message send from server is: {recv_data.decode('UTF-8')}")
socket_client.close()