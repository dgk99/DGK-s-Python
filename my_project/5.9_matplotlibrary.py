# 필요한 라이브러리를 임포트 한다.
import matplotlib.pyplot as plt # Matplotlib 그래프 사용
import random


# 그래프에 넣을 임의의 데이터 생성
# x_value에 1부터 99까지의 값을 순차적으로 반복하여 출력
x = [x_value for x_value in range(1, 100)]
# y_value에 1부터 100사이의 랜덤한 수를 리스트에 저장
y = [random.randint(1, 100) for y_value in range(1, 100)]

# 그래프에 사용할 폰트 설정
plt.rc('font', family = 'Malgun Gothic')

# 그래프에 사용될 축의 데이터 입력 -> x는 위에서 지정한 1부터 99까지의 수
#                                   y는 1부터 99까지의 랜덤한 수 하나
plt.plot(x, y)

# 그래프 제목 설정
plt.title('기본 선형 그래프')

# 그래프 x축 이름 설정
plt.xlabel('X 축')

# 그래프 y축 이름 설정
plt.ylabel('Y 축')

# 그래프 출력 명령어
plt.show()