import cv2

# 웹캠 연결 (일반적으로 0번 장치)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("웹캠에서 영상을 받아올 수 없습니다.")
        break
    
    # 화면에 출력
    cv2.imshow('Webcam', frame)
    
    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
