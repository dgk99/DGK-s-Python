import socket

#socket생성(ipv4 or ip6,tcp or udp)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connenct(서버주소,서버 포트)
client_socket.connect(("127.0.0.1",5500))