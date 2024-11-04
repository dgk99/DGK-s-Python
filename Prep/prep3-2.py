
# 우리가 구해야 할 건, 총 점수
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    
    total_class_hours = hours_per_week * 15
    
    if tardy_count >= 3: # 지각 처리 계산식
        absence_hours += int(tardy_count / 3)
        
    Attendance_score = round(20-(20 * absence_hours / total_class_hours), 2)
    
    if absence_hours > (hours_per_week * 15 / 4): # 결석 처리 계산 식
        Attendance_score = "F (학점 미부여)"
        
    return Attendance_score

# 주당 수업 시간을 입력받는다
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
# 결석한 총 시간을 입력받는다
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
# 지각 횟수를 입력받는다
tardy_count = int(input("지각 횟수를 입력하세요: "))

Attendance_score = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)

print("당신의 출석 점수는",Attendance_score,"점입니다.")

# 총 점수는 20점-(20x결석시간 수/총 수업시간 수)
# 총 수업시간은 주당 수업 시간 x 15
# 20점 - (20 x absence_hours / hours_per_week x 15)

# 지각 처리 조건(결석보다 먼저 처리되어 결석 시간을 만들어야함)
# tardy_count % 3 == 0:
# 지각이 3회일 때 마다 결석 시간이 1시간씩 늘어나야 함
# absence_hours += 1

# 결석 처리 조건
# absence_hours > (hours_per_week x 15) / 4:
# 무조건 F 출력