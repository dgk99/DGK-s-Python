# 동사 그룹 맞추기 프로그램
# 일본어 문법 시간에 배운 동사를 그룹별로 나누는 프로그램을 짜 보자
# 모든 동사를 모아보자
dongsa = ["する", "来(く)る", "食(た)べる", "教(おし)える", "疲(つか)れる", "信(しん)じる", "晴(は)れる", "寝(ね)る", "見(み)る", "できる", "起(お)きる", "着(き)る","飲(の)む","持(も)つ","買(か)う","話(はな)す","死(し)ぬ", "会(あ)う","行(い)く","遊(あそ)ぶ","待(ま)つ","書(か)く","ある","乗(の)る","取(と)る","残(のこ)る","作(つく)る","始(はじ)まる","勉強(べんきょう)する","曲(まが)る","変(か)わる","頑張(がんば)る","参加(さんか)する","わかる","切(き)る","入(はい)る","要(い)る","知(し)る","走(はし)る","帰(かえ)る"]

# 그룹은 총 3개이고, 각각의 특징을 가지고 있다.
# 1그룹 - 1그룹에서도 3개의 특징으로 나뉜다.
#         1. る가 없으면 1그룹
#         2. a단,u단,o단 + る라면 1그룹
#         3. 예외 동사들()
# 2그룹 - i단,e단 + る 이면 2그룹
# 3그룹 - 단 2개. する、来(く)る
import random
# 사용자에게 랜덤으로 하나의 동사를 보여주고, 이 동사가 어디 그룹에 속해있는지 입력값을 받는다.
while True:
    dongsa_print = random.choice(dongsa)
    print(dongsa_print)
    input_value = input("이 동사의 그룹을 입력하시오: ")
    
    if (dongsa_print == "する" or dongsa_print == "来(く)る" or dongsa_print =="勉強(べんきょう)する" or dongsa_print =="参加(さんか)する" ) and input_value == "3" :
        print("정답입니다")
        print()
    
    elif (dongsa_print == "食(た)べる" or dongsa_print == "教(おし)える" or dongsa_print == "疲(つか)れる" or dongsa_print == "信(しん)じる" or dongsa_print == "晴(は)れる" or dongsa_print == "寝(ね)る" or dongsa_print == "見(み)る" or dongsa_print == "できる" or dongsa_print == "起(お)きる" or dongsa_print == "着(き)る") and input_value == "2" :
        print("정답입니다")
        print("い,え단 + る이기에 2그룹입니다")
        print()
        
    elif (dongsa_print == "飲(の)む" or dongsa_print =="持(も)つ" or dongsa_print =="買(か)う" or dongsa_print =="話(はな)す" or dongsa_print =="死(し)ぬ" or dongsa_print =="会(あ)う" or dongsa_print =="行(い)く" or dongsa_print =="遊(あそ)ぶ" or dongsa_print =="待(ま)つ" or dongsa_print =="書(か)く") and input_value == "1":
        print("정답입니다")
        print("る가 없기 때문에 1그룹입니다")
        print()
        
    elif (dongsa_print =="ある" or dongsa_print =="乗(の)る" or dongsa_print =="取(と)る" or dongsa_print =="残(のこ)る" or dongsa_print =="作(つく)る" or dongsa_print =="始(はじ)まる" or dongsa_print =="曲(まが)る" or dongsa_print =="変(か)わる" or dongsa_print =="頑張(がんば)る" or dongsa_print =="わかる") and input_value == "1":
        print("정답입니다")
        print("あ,う,お단 + る이기에 1그룹입니다")
        print()
        
    elif (dongsa_print =="切(き)る" or dongsa_print =="入(はい)る" or dongsa_print =="要(い)る" or dongsa_print =="知(し)る" or dongsa_print =="走(はし)る" or dongsa_print =="帰(かえ)る") and input_value == "1":
        print("정답입니다")
        print("이 동사들은 い,え단 + る이지만 예외적으로 1그룹입니다.")
        print()
    
    elif input_value == "5":
        break
    
    else:
        print("오답입니다")
        print()

# 입력받은 값이 오답이면, 이 동사는 어느 그룹인지 정답을 알려주고 새 문제를 낸다.
# 입력받은 값이 정답이면, 정답이라고 하고 새 문제를 낸다.
# 프로그램 종료를 입력하면 프로그램이 종료된다.

