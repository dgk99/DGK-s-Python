import socket
import threading

def handler_client(client_socket, client_addr): # 스레드에 의해서 호출 됨. 함수에는 소켓의 값을 인자값으로 넣어줌.
    # 클라이언트로 부터 데이터 수신
    while True: 
    # 한 번 실행하고 종료되기 때문에 계속 서버가 클라이언트로부터 온 메시지를 돌려줘야 하기에 반복문을 사용
        rcvd_data = client_socket.recv(1024).decode('utf-8')

        # 클라이언트가 소켓 종료를 호출하면 반복문 종료
        # 클라이언트가 소켓 종료를 호출하면 -> 빈 문자열 메시지가 날아옴 = 상대방이 연결 종료를 요청한 것.
        if not rcvd_data: # 클라이언트가 close를 호출하면 참이 되어 반복문 종료
            print("[Close from client]")
            break
        
        print(f"[rcvd_data ({client_addr})]: {rcvd_data}")

        # 수신된 데이터를 전송
        client_socket.sendall(rcvd_data.encode('utf-8'))
        # 수신된 데이터를 다시 클라이언트로 전송

HOST = "127.0.0.1" # 서버의 IP 주소 -> 문자형
PORT = 12345 # 포트 주소 -> 정수형
num_of_threads = 0

# socket 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP용 소켓 생성

# bind(현재 소켓에다가 ip, port 주소를 결합)
server_socket.bind((HOST, PORT))

# listen
server_socket.listen(1)


print(f"[Listen] {HOST}, {PORT}")

while True:
    # accept -> 새로운 소켓을 생성
    client_socket, client_addr = server_socket.accept()

    print(f"[Accept] {client_addr}")
    # send, receive 진행
    # echo server
    # clinet로 부터 데이터 수신

    # 새로운 스레드 생성
    client_thread = threading.Thread(target=handler_client, args=(client_socket, client_addr))
    
    num_of_threads += 1
    print(f"쓰레드 생성 : {num_of_threads}")

    
    # 생성된 스레드 실행
    client_thread.start()


client_socket.close()
server_socket.close()