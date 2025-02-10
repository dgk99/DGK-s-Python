# 소켓, 스레드 import
import socket
import threading

# ip, port 주소 설정
HOST = '127.0.0.1'
PORT = 12345

# 서버 소켓 생성(IPv4, TCP의 소켓)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 소켓 바인드
server_socket.bind((HOST, PORT))

# 클라이언트의 연결을 듣기
server_socket.listen(1)

# 클라이언트 소켓과 주소를 연결
client_socket, client_addr = server_socket.accept() 

# 반복문에 사용할 전역변수 선언
is_active = [True]

# 데이터 전송
# 데이터 전송 함수
def handler_tx(client_socket:socket.socket):
    # 계속 전송하기 위해 while문 사용
    while is_active[0]:
        # 사용자 메시지 입력
        send_msg = input("입력: ")
        
        # 사용자가 종료를 입력하면, 반복문 탈출
        if send_msg.lower() == 'exit':
            # 클라이언트 소켓 종료
            client_socket.close()
            # 전역변수 false로 전환 -> 반복문 종료
            is_active[0] = False
            # 탈출
            break
        
        # 메시지 encode 해서 보내기
        client_socket.sendall(send_msg.encode('utf-8'))

# 데이터 수신
# 데이터 수신 함수
def handler_rx(client_socket:socket.socket):
    # 계속 수신하기 위해 while문 사용
    while is_active[0]:
        # 서버에서 온 메시지를 decode해서 수신
        rcvd_msg = client_socket.recv(1024).decode('utf-8')
        
        # 서버에서 연결을 끊으면 반복문 종료
        if not rcvd_msg:
            break
        
        # 받은 메시지 출력
        print(f"Received msg: {rcvd_msg}")
    
    # 전역변수 false
    is_active[0] = False


# 수신, 송신 스레드 생성
thread_tx = threading.Thread(target=handler_tx, args=(client_socket,))
thread_rx = threading.Thread(target=handler_rx, args=(client_socket,))

# 스레드 시작
thread_tx.start()
thread_rx.start()

# 스레드가 끝날 때 까지 잠시 정지
thread_tx.join()
thread_rx.join()