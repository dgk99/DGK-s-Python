import socket
#소켓생성(tcp or udp,ip주소 버전 :v4 or v6)
#TCP:socket.SOCK_STREAM
#UDP:socket.SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind(ip주소,port주소)
server_socket.bind(("127.0.0.1",5500))

#listen(큐의 개수)
server_socket.listen(5)

print(f"listen on 127.0.0.0.1:5500")

#accept(), ->사용자로 부터 연결 요청을 받았을떄 ->새로운 소켓 생성
#클라이언트 ->connect()
client_socket, client_addr = server_socket.accept()

print(f"[client ip address] : {client_addr}")

# 구현해야 하는 알고리즘

# 클라이언트로부터 메시지를 수신
# 현재 연결된 client로 부터 데이터를 가져오는 함수
# Q1. 리시브 함수는 동기인가 비동기인가 A. 동기 함수이다.
# Q2. 데이터를 가져오는데 자료형은 무엇인가? A. byte형

# 왜 byte형으로 넘어온걸까? 
# 네트워크에서 데이터를 보낼때는 bit단위로 보내야 한다.
# bit는 byte단위로 묶음. 운영체제에서 처리하는 최소한의 단위가 byte니깐.
# 소켓에서 byte단위로 데이터를 주고 받음.

rcvd_data = client_socket.recv(1024) # ()의 숫자는 최대 몇 byte를 가져올지에 대한 의미

print(f"type 0f rcvd_Data : {type(rcvd_data)}")
# 수신한 메세지를 클라이언트로 전송