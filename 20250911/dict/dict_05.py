# 선거 시스템
# 유권자들은 투표를 진행결과를 리스트에 저장
# ex 1,2,3
# 투표는 순환문은 이용해서 유권자가 10이라면 10번 순환하면서 후보자(1~5)선택
# [1,1,2,3,4,1,5,1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
cadidate = ['홍길동', '이순신', '강감찬','율곡', '신사임당']
vote = [] # 투표함
counts = 10 # 유권자 명수

def toopyo():
    '''
    10명의 유권자에게 투표 입력값 받기
    '''
    for _ in range(0,counts+1):
        user_input = int(input('투표를 하세요 (1~5) : '))
        vote.append(user_input)
        # ^ 잘못입력했을 경우 다시 안내를 하는 코드 작성해보기.

def cacul(vote):
    '''
    투표결과 계산기
    '''
    hong = vote.count(1)
    yee = vote.count(2)
    gang = vote.count(3)
    eyul = vote.count(4)
    sin = vote.count(5)
    # 이중에서 제일 큰수를 구하는 법?  
    if hong * 5 > (yee + gang + eyul + sin):
        return '홍길동'
    elif yee * 5 > (hong + gang + eyul + sin):
        return '홍길동'
    elif gang * 5 > (hong + yee + eyul + sin):
        return '강감찬'
    elif eyul * 5 > (hong + gang + yee + sin):
        return '강감찬'
    elif sin * 5 > (hong + gang + eyul + yee):
        return '심사임당'

# 메인 코드
toopyo()
print(cacul(vote))