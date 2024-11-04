# 가상 주식 거래 시뮬레이션

# 사용자가 입력해야 하는 정보
# 초기 자본금 initial capital
ic = int(input("초기 자본금을 입력하세요: "))
# 주식의 구매 가격 stock purchase price
spp = int(input("주식 가격을 입력하세요: "))
# 구매할 주식의 수 Number of shares to be purchased
nsp = int(input("구매할 주식 수를 입력하세요: "))
# 판매할 때의 주식 가격 the price of shares to be sold
pss = int(input("판매할 때의 주식 가격을 입력하세요: "))



# 요구 사항
def stock_trading_calculator(ic, spp, nsp, pss):
    # 총 구매 비용Total Purchase Cost = 구매 가격 * 주식 수
    tpc = spp * nsp
    # 구매 후 남은 자본금capital remaining after purchase = 초기 자본금 - 총 구매 비용
    crap = ic - tpc

# 총 판매 금액 = 판매할 때의 주식 가격 * 주식 수, 여기서 총 구매 비용을 빼서 예상 이익 및 손실
# 구매 후 남은 자본금과 예상 이익 및 손실을 출력
#