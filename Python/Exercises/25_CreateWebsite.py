#import socket


#mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET é o website, SOCK_STREAM é a porta (80)
#mysocket.connect(('data.pr4e.org', 80))  # Ligar o site pela porta 80
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode()
#mysocket.send(cmd)

#while True:
#    data = mysocket.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode())
#mysocket.close()

# Outra forma de fazer:

import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip)