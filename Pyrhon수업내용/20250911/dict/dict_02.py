# list, set, tuple, dict

# 리스트를 딕셔너리로 형변환
result = dict([['name' , 'age'],['홍길동', 20]])
print(type(result))
print(result)

#
# 다른 하나는 값에 해당하는 집합
#이걸 dict 구조로 만들려면
names = ['홍길동','이순신','강감찬']
scores = [100,99,98]
students = {}
# 비어있는 dict 변수를 생성
# 변수['키'] = 값 형태로 딕셔너리 생성 -> 순환문을 통해서
# 딕셔너리내에 값을 생성하기 위해선 저 형태로 부여하는구나,
# 아니면 리스트로 2개씩 짝지어서 모아두고 형변환을 해도되고

count = 0
for name in names:
    students[name] = scores[count]
    count += 1

for i in range(len(names)):
    students[names[i]] = scores[i]

# 딕셔너리 생성
food = {'비빔밥' : 10000, '햄버거' : 7000, '고등어 정식' : 12000}
# 딕셔너리에서 값을 출력
print(food['비빔밥'])
# 딕셔너리에서 값을 추가
print(food)
food["국수"] = 7000
print(food)
# 딕셔너리 삭제
del food["햄버거"]
print(food)
# 딕셔너리 특정 키의 데이터를 수정
food["비빔밥"] = 11000
print(food)