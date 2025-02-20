import json

# JSON 데이터 생성 (파이썬 딕셔너리 -> JSON 문자열)
chat_message = {
    "type": "private_message",
    "from": "Mingyu",
    "to": "God",
    "message": "Dear, God",
    "timestamp": "1023-01-01T08:00:00"
}

json_message = json.dumps(chat_message, indent=4)
print("JSON 송신 데이터: ")
print(json_message)

# JSON 데이터 파싱 (JSON 문자열 -> 파이썬 딕셔너리)
received_message = json.loads(json_message)
print("\n 수신된 메시지 데이터: ")
print(f"Type: {received_message['type']}")
print(f"from: {received_message['from']}")
print(f"To: {received_message['to']}")
print(f"Message: {received_message['message']}")