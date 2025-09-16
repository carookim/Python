# 파일 위치 : 01.py
# ! 리스트 컴프리헨션 여러가지 사례 복습할때 해보기

# 1] 리스트 컴프리 핸션

# [ 표현식 for 변수 in 반복가능객체 ]
# 표현식 : 리스트에 들어갈 값. 여기서는 i

# for 변수 in 반복가능객체 : 반복할 범위나 컬렉션. 여기서는 range(1, 11)

# 이렇게 쓰면 반복문 한 줄로 리스트를 만들 수 있음


import random
# 1) 리스트 컴프리핸션 기본예제(1) - for문
# 기존 함수 구문
total = []
for i in range(1,11):
    total.append(i)
print(total)

# 이걸 한줄로 표현
print( [ i for i in range(1,11) ] )

# 2) 리스트 컴프리핸션 기본예제(2)
# 기존 함수 구문
total = []
for i in range(5):
    total.append(random.randint(1,10))
print(total)

# 이걸 한줄로 표현
import random
print([random.randint(1,10) for i in range(5)])

# 3)  if 구문을 사용하면서 한줄로 정리하기
# 기존 함수 구문
list_1 = []
for i in range(5):
    if i % 2 == 0:
        list_1.append(i)
print(list_1)

# 이걸 한줄로 표현
print([ i for i in range(5) if i % 2== 0])
# 'if i % 2== 0' 이 조건에 해당할때에만 list에 포함한다.

# 4) enumerate와 if 구문을 활용하여 한줄로 정리하기
list_1 = [1,2,3,1,2,3,5,4,8]
# 값 2에 해당하는 인덱스를 찾아서 리스트로 반환
# [1,4]

# 이걸 한줄로 표현
print([ idx for idx,value in enumerate(list_1) if value == 2]) # for i in range() 여기서 i에 두가지 변수가 들어간 경우 ^

# 5) if, else 구문 한줄로 정리하기
# 기존 함수 구문
age = 20
if age >= 18:
    result = '성인'
else:
    result = '미성년'
print(result)

# 이걸 한줄로 표현
result = '성인' if age >= 18 else '미성년' # 삼합연산자

# 6)
list_1 = [1,2,1,5,3,2,1,54]