# 모듈과 패키지
# main.py

# 함수 : 전체 알고리즘을 '모듈화' 하기 위해서 생김
# 모듈은 스크립트 파일을 의미한다. 스크립트 파일 내에는 함수, 변수 등으로 이루어져 있다.
# 같은 속성을 가진 기능들을 .py로 묶어, 내가 필요할 때 마다 호출하여 사용할 수 있다.
# 모듈이 없다면, 함수를 만들어도 다른 곳에 사용할 수 없다.
# 패키지는 여러 개의 같은 속성을 가진 모듈들을 하나로 관리하는 것을 의미한다.

# import random

# random.randint(2, 10)

# print(random.test_1)

# from bar import file_name as b_name
# import foo

# foo.print_name(b_name)

# import sys

# print(type(sys.path))

# for path in sys.path:
#     print(path)
    
    
# 매직 변수 : 파이썬 인터프리터가 만든 변수
# __name__ 해당 스크립트 파일을 실행하면, __main__이 출력된다.

import bingo # __main__ -> bingo

print(__name__)

