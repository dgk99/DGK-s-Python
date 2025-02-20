# 리스트에서 인덱스 값은 0부터 시작해서 순차적으로 나열된 key 값이다. 
# 특정 값을 찾아가기 위해 시간이 많이 걸림.

# index값을 0와 양의 정수가 아닌 의미 있는 값으로 사용하고 싶다.
# 특정 key값을 hash-function을 이용해 길이가 고정된 난수 발생.

# bar = {'김민규' : 12345, '하루나' : 67890, '김민정' : 98765, '김민규' : 5555, '김민정' : 1111}

# print(bar['김민규'])

# print(bar.items())

# for key, value in bar.items():
#     print(f"key: {key}, value: {value}")
    
# del bar['김민규']

#Python

import json

bar = {'name' : 'dgk', 'age' : 26, 'roomnum' : [405]}

# 네트워크로 전송 -> 문자열(Text) -> JSON
# bar는 메모리에 존재하는 데이터 -> JSON Serializer
# -> JSON 기반 Text

# serializing
json_str = json.dumps(bar)

print(type(json_str), json_str)

# parsing -> 예외
rcvd_data = json.loads(json_str)

print(rcvd_data['phone'])
print(rcvd_data.get('phone'))

print(type(rcvd_data['age']), type(rcvd_data['roomnum']), type(rcvd_data['name']))