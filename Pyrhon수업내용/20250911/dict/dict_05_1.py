## 강사님이 작성해주신 코드, 딕셔너리 활용
cadidate = ['홍길동','이순신','강감찬','율곡','신사임당']
vote = []
counts = 10
result = {}
# for _ in counts:
#     vote.append(int(input('투표를 하세요(1~5) : ')))
vote = [1,2,3,4,2,2,1,2,2,4]
print(f'vote = {vote}')

# dict 기능을 이용 $
# result가 빈 딕셔너리 형식을 가지고 있고, {}
# result[i] += 1에서 왼쪽값이 key, 오른쪽값이 value가 되어 딕셔너리가 된다.
for i in vote:
    if i in result: 
        result[i] += 1
    else:
        result[i] = 1
print(f'result = {result}')

print(max(result)) #  최댓값을 구하는 max 메소드, 최솟값을 구하는 min 메소드

# 딕셔너리에서 값을 가져오는 방법
# 1) 직접 입력 :딕셔너리변수.['키값'] 없으면 에러가 뜬다.
# 2) .get 메소드 :딕셔너리변수.get('키값') 없으면 None이 뜬다.
    # .get(x,y) x는 키값, 그 x 키값이 없는 경우 y 를 출력

# def find_max(result, key = result.get) # max(x,y) ^ x와 y 값을 비교해서 반환한다. a,b,c,d 이렇게도 가능하다. ^

'''
------------------------------------------------
'''

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
# for _ in counts:
#     vote.append(int(input('투표를 하세요(1~5) : ')))
vote = [1,2,3,4,2,2,1,2,2,4]
print(f'vote = {vote}')

# dict 기능을 이용
for i in vote:
    if i in result: 
        result[i] += 1
    else:
        result[i] = 1
print(f'result = {result}')

# 키의 값을 가져올때..  딕셔너리변수['키값']  없으면 에러
# 딕셔너리변수.get('키값')  없으면 None
max_key =  max(result, key=result.get )
# 당선자  key - 1

print(f'당선자 : {cadidate[max_key-1]} 득표수 : {result[max_key]}')

## 딕셔너리와 메소드들 사용해서 깔끔하게 만들어보기 ^