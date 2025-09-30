# https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 언어 : 파이썬 / 레벨 : 1 /정답률 : 89% 
# 옷가게 할인 받기

# 문제 설명
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 10 ≤ price ≤ 1,000,000
# price는 10원 단위로(1의 자리가 0) 주어집니다.
# 소수점 이하를 버린 정수를 return합니다.

# 입출력 예
# price	result
# 150,000	142,500
# 580,000	464,000

# 입출력 예 설명
# 입출력 예 #1
# 150,000원에서 5%를 할인한 142,500원을 return 합니다.

# 입출력 예 #2
# 580,000원에서 20%를 할인한 464,000원을 return 합니다.

def solution(price):
    if price >= 500000:
        answer = int(price*(1-0.2))
    elif price >= 300000:
        answer = int(price*(1-0.1))
    elif price >= 100000:
        answer = int(price*(1-0.05))
    else:
        answer = price
    return answer

# 다른 사람 풀이 1 - 딕셔너리 사용
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
# 다른 사람 풀이 2 ^
def solution(price):
    return (100 - len([1 for k in [100000, 300000, 500000, 500000] if k<=price])*5) * price // 100

# 리스트 컴프리헨션 이용 

def soultion(price):
    return int((100 - len([1 for k in [100000, 300000, 500000, 500000]if k <- price])*5) * 0.01 * price)

print(soultion(200000))