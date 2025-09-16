# 파일 위치 : dict_05.py, dict_05_1.py

# 9] 딕셔너리 활용 문제 : 선거 시스템

# (1)본인작성
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

# (2) 강사님이 작성해주신 코드, 딕셔너리 활용
# 선거시스템
# 유권자  들은 기호로 투표를 진행 결과를 리스트에 저장
#  ex 1,2,3
# 투표는 순환문은 이용해서 유권자가 10이라면 10번순환하면서 후보자(1~5)선택
# [1,1,2,3,4,1,5,1]
# 리스트에있는 각 번호의 횟수를 구해서 당선자를 출력

cadidate = ['홍길동','이순신','강감찬','율곡','신사임당']
vote = []
counts = 10  # 유권자
result = {}  # 투표카운트 
# for _ in counts: # 10번 반복 : _가 0~9로 대입되면서 10번 반복 
#     vote.append(int(input('투표를 하세요(1~5) : '))) # vote 빈리스트에 유권자에게 투표값을 받는다.

vote = [1,2,3,4,2,2,1,2,2,4] # 예시 투표결과
# print(f'vote = {vote}') # 확인용 출력

# dict 기능을 이용
for i in vote: # 예시 투표결과를 기준으로, i는 0,1,2,3,4,5,6,7,8,9 순으로 대입되며 10번 반복
    if i in result: # 딕셔너리 내부에 키가 있다면, 
        result[i] += 1 # 기존 해당 키에 쌍을 한 값에 +1 해서 누적한다.
    else:           # 딕셔너리 내부에 키가 없다면,
        result[i] = 1 # 처음 등장한 것이므로 result[키] = 값 형식으로 새로 만든다. ( 값을 1로 초기화 : 여기서 초기화는 초기값 할당에 해당된다.)
print(f'result = {result}')

# 딕셔너리에서 값을 가져오는 방법
# 1) 직접 입력 :딕셔너리변수.['키값'] 없으면 에러가 뜬다.
# 2) .get 메소드 :딕셔너리변수.get('키값') 없으면 None이 뜬다.
    # .get(x,y) x는 키값, 그 x 키값이 없는 경우 y 를 출력(default 출력은 None)

max_key =  max(result, key=result.get ) # 최댓값을 구하는 max 메소드, 최솟값을 구하는 min 메소드
# 당선자 번호 : key - 1                  # max(iterable, key=function) : 파이썬에서 가장 큰 값을 반환할 때 사용하는 함수
                                        # x : iterable 자료형, y : 비교 기준
print(f'당선자 : {cadidate[max_key-1]} 득표수 : {result[max_key]}')

# 여기서 새로 배운 함수와 메소드 : 최댓값과 최솟값, 값을 가져오는 메소드
# max() / min()
# .get( , )

def find_max(result):
    return(max(result, key=result.get))

print(find_max(result))

## 딕셔너리와 메소드들 사용해서 깔끔하게 만들어보기 ^