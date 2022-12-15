#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def server_start():
    try:
        LOCALSHOT = "127.0.0.1" # IP - адрес
        PORT = 2000 # порт 
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((LOCALSHOT, PORT))
        server.listen(4)
        while True:
            print('Запущен...')
            clientsock, clientAddress = server.accept()
            data = clientsock.recv(1024).decode('utf-8')
            #print(data)
            msg = obrabot(data)
            clientsock.send(msg)
            clientsock.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Отключение...")
    
def obrabot(request_data):
    HDRS ='HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 ='HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        with open('views'+path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Такой страницы не существует...').encode('utf-8')

if __name__ == '__main__':
    server_start()


# In[ ]:




