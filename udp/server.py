import socket
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
s = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
s.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    data = math.factorial(int(data ))
    s.sendto(str(data),addr) 
