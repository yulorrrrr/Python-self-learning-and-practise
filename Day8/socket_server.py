import socket
socket_server = socket.socket()

# Bind the server socket to a specified IP address and port
socket_server.bind(("localhost", 6666)) 
socket_server.listen(1) # Number of connections received：1
print("Server listening on localhost:6666 ...")

#waitingfor client's response
'''
result: tuple = socket_server.accept()
conn = result[0] #Client–server connection object
address  = result[1] #the address information of client
-> '''
conn, address = socket_server.accept()
print(f"Already accept client's connection, client's information: {address} ")


while True:
    #accept client information
    data:str = conn.recv(1024).decode("UTF-8")
    print(f"The message sent by the client is: {data}")

    msg_ = input("please enter the message you want to send to client")
    if msg_ == 'exit':
        break
    conn.send(msg_.encode("UTF-8"))

conn.close()
socket_server.close()

