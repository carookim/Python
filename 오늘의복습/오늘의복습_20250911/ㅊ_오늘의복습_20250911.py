# 파일 위치 : dict_02.py

# 8] 딕셔너리 형변환

# 딕셔너리 타입 확인하기
result = dict([['name' , 'age'],['홍길동', 20]])
print(type(result))
print(result)
print()

# 리스트 -> 딕셔너리
# 두개의 리스트  한개는 키에 해당하는 값들의 집합
# 다른 하나는 값에 해당하는 집합
# 이걸 dict 구조로 만들려면
names = ['홍길동','이순신','강감찬']
scores = [100,99,98]
students = {} # 비어있는 dict 변수 sutdents를 생성

# 변수['키'] = 값 형태로 딕셔너리 생성

# 1) 순환문 사용
count = 0
for name in names:
    students[name] = scores[count]
    count += 1

for i in range(len(names)):
    students[names[i]] = scores[i]

# 2) zip() + dict() 사용
students = dict(zip(names), scores) # 파이썬에서 두 개 이상 시퀀스를 “묶어주는” 함수
print(students)                     # zip 내부 인자 → 반복 가능한 객체만 가능
                                    # zip 결과 → 이터레이터 → 리스트, 튜플, 세트, 딕셔너리 등 반복 가능한 구조로 변환 가능
                                    # 주의: dict는 (key,value) 길이가 2인 튜플이 필요

# 3) 딕셔너리 컴프리헨션 ^

# 다시 짚어보는 내용 :

# 딕셔너리 생성
food = {'비빔밥' : 10000, '햄버거' : 7000, '고등어 정식' : 12000}

# 딕셔너리에서 값을 출력
print(food['비빔밥'])
print()

# 딕셔너리에서 값을 추가
print(food)
food["국수"] = 7000
print(food)
print()

# 딕셔너리 삭제
del food["햄버거"]
print(food)
print()

# 딕셔너리 특정 키의 데이터를 수정
food["비빔밥"] = 11000
print(food)

# 여기서 새로 배운 함수 :
# zip()