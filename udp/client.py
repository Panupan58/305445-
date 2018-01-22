import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "4"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

s = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
s.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, server = s.recvfrom(1024)
print "result =",data
