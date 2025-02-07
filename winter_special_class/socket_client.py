import socket

HOST = "127.0.0.1"
POST = 12345

# socket 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP4V의 TCP 소켓 생성

# connect
client_socket.connect((HOST, POST))
# 내가 보내고 싶은 곳의 ip와 post 주소 설정

while True:
    # 사용자로부터 데이터 입력
    send_msg = input("Input text: ")
    # 보내고 싶은 메시지 입력 칸
    
    if send_msg.lower() == "exit":
    # 들어온 알파벳을 소문자로 받기 위해 lower함수 사용
        break

    # 입력된 데이터를 서버로 전송
    client_socket.sendall(send_msg.encode("utf-8"))
    # 데이터를 전송하기 위해 byte형으로 encode해서 보내야 함

    # 서버로부터 수신한 데이터를 출력
    rcvd_msg = client_socket.recv(1024).decode("utf-8")

    print(f"[Client rcvd data]: {rcvd_msg}")

client_socket.close()
print("클라이언트 종료")
