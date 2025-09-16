# 파일 위치 : set_02.py

# 5] 집합 형변환(2)

# 1)
import random

list_a = random.sample(range(10),6)
list_b = random.sample(range(10),4)

find_list = [] # 담을 빈 리스트 생성

# list_a와 list_b 사이에 서로 동일하는 값이 있는지를 확인하는 코드 작성
for a in list_a:
    for b in list_b: # list_a와 list_b 내부의 값을 순차적으로 매칭, list_a와 list_b 각 객체전체에 연산을 거치도록 설정
        if a == b: # list_a와 list_b 내부에 동일한 값이 있으면 find_list에 추가하도록 연산내용 설정
            find_list.append(a)

set(find_list) # 집합의 특성을 사용하여, 중복되는 값을 제거하기.

print(f'list_a = {list_a}')            
print(f'list_b = {list_b}')            
print(f'find_list = {find_list}')         
print(f'set(find_list) = {set(find_list)}')

# 2)
# 15라인에서 set을 사용하지 않고 원래 로직(10~13라인)을 개선해서 
# find_list에 중복값이 저장되지 않도록 코드 작성

list_c = random.sample(range(10),6)
list_d = random.sample(range(10),4)

find_list = [] # 담을 빈 리스트 생성

# list_c와 list_d 사이에 서로 동일하는 값이 있는지를 확인하는 코드 작성
for c in list_c:
    for d in list_d: # list_c와 list_d 내부의 값을 순차적으로 매칭, list_c와 list_d 각 객체전체에 연산을 거치도록 설정
        if c == d: # list_c와 list_d 내부에 동일한 값이 있으면 find_list에 추가하도록 연산내용 설정
            find_list.append(c)
    find_list_set = set(find_list) # for문을 통해 list_c와 list_d 각 객체전체에 연산을 거치고 난후, 마지막 연산내용 설정

print(f'list_c = {list_c}')            
print(f'list_d = {list_d}')            
print(f'find_list_set = {find_list_set}')  

# 여기서 새로 배운 메소드 :
# random.sample( , )