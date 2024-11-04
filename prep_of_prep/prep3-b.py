# 출석 점수 프로그램
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    # 총 수업 시간 계산법
    # 시수/주 x 15
    total_class_hours = hours_per_week * 15
    
    if tardy_count >= 3 :
        absence_hours += int(tardy_count / 3)
    
    # 출석 점수 계산법
    # 20점 - (20 x 결석시간 수 / 총 수업시간 수)
    Attendance_score = 20 - (20 * absence_hours / total_class_hours)
    

    if absence_hours > (total_class_hours / 4) :
        grade = "F (학점 미부여)"
        return grade
        
    return Attendance_score
    

# 지각 처리 규칙
# 지각 3회는 결석 1시간으로 처리
# 결석 처리 규칙
# 결석시수가 총 수업시수의 1/4를 초과할 경우 학점 미부여(F처리)

# 사용자로부터 주당 수업시간(시수/주)
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

# 결석한 총 시간
# 지각 횟수를 입력받습니다.

Attendance_score = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)


print("당신의 출석 점수는",calculate_attendance_score(hours_per_week, absence_hours, tardy_count),"점입니다.")