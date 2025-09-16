# 파일 위치 : set_03.py

# 6] 집합연산

# 6]-1 random 모듈기능 random.sample,random.randit

# random.sample(시퀀스자료형,b)의 기능
# 겹치지 않게 b개의 원소를 시퀀스 자료형에서 무작위로 뽑아 리스트로 반환하는 함수

import random
list_a = random.sample(range(11),7) # 0~10 중복되지 않은 객체 7개
list_b = random.sample(range(11),7)
# 중복을 허용하면서 0 ~ 10 임의의 7개의 값 추출

# random.randit(a,b)의 기능
# a 이상 b 이하의 정수를 무작위로 하나 뽑아 반환하는 함수
# 임의의 범위를 정의
list_c = []
for _ in range(7): # i의 역할이 없다 는 것을 표현하는 법 i -> _
    list_c.append(random.randint(0,10)) # 0 이상 10 이하의 정수를 무작위로 하나 뽑아 반환


# 6]-2 집합연산자

# set에서 사용 가능한 연산자 : |, &, -
# set에서 사용 가능한 메소드 : .union(), .intersection(), .difference()

# 합집합
    # 연산자 | (파이프 연산자) -> or
    set_a = {1,2,3}    
    set_b = {3,4,5}    
    union_set = set(list_a) | set(list_b)
    print(union_set)
    # 매서드 .union()
    # # 매서드로도 접근이 가능 하다.
    union_set = set_a.union(set_b)
    print(union_set)
          
# 교집합
set_a, set_b = {1,2,3,4},{2,3,5}
    # 연산자 &    -> and
print(set_a & set_b)    
    #  메서드  .intersection()
print(set_a.intersection(set_b))    

# 차집합    
    # 연산자 - 
print(set_a  - set_b)    
    #  메서드  .difference()
print(set_a.difference(set_b))

# set_a가 set_b보다 작을 때는? ^
set_a, set_b = {2,3,5},{1,2,3,4}
print(set_a  - set_b)
print(set_a.difference(set_b))

# 여기서 새로 배운 메소드 : 랜덤.메소드와 집합.메소드
# 랜덤.메소드
# random.randint( , )

# random.sample( , )

# 집합.메소드
# .union()
# .intersection()
# .difference()