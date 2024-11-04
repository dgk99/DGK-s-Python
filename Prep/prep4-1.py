def stocktrading(initialcapital, purchaseprice, numberofpurchased):
    
    #1. 주식 구매 비용 계산 '총 구매 비용' 
    # 총 구매 비용 = 주식의 구매 가격 * 구매할 주식의 수
    totalpurchasecost = purchaseprice * numberofpurchased
    
    #2. 남은 자본금 계산 '남은 자본금'
    # 남은 자본금 = 초기 자본금 - 총 구매 비용
    remainingcapital = initialcapital - totalpurchasecost
    
    return remainingcapital


#4. 결과 출력(남은 자본금, 예상 이익 또는 손실)
# print(float("구매 후 남은 자본금",remainingcapital))
# print(float(예상 이익 : ,anticipated))

#입력받아야 하는 내용
#1. 초기 자본금
initialcapital = int(input("초기 자본금을 입력하세요: "))

#2. 주식의 구매 가격
purchaseprice = int(input("주식 가격을 입력하세요: "))

#3. 구매할 주식의 수
numberofpurchased = int(input("구매할 주식의 수를 입력하세요: "))

#4. 판매할 때의 주식의 가격
soldprice = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 판매 후 예상 값
salesprofit = soldprice * numberofpurchased - (purchaseprice * numberofpurchased)
# 예상값이 0보다 크면 이익, 작으면 손실로 출력
if salesprofit > 0:
    salesprofit_words = "예상되는 이익입니다."
else:
    salesprofit_words = "예상되는 손실입니다."
    
remainingcapital = "{:.2f}".format(float(stocktrading(initialcapital, purchaseprice, numberofpurchased)))
salesprofit = "{:.2f}".format(float(salesprofit))

print("구매 후 남은 자본금: ",remainingcapital)
print("예상 이익 : ",salesprofit)
print(salesprofit_words)