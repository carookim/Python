# set의 집합연산
import random

list_a = random.sample(range(10),6) # sample(,) 형식 ^
list_b = random.sample(range(10),4)

find_list = [] # list_a와 list_b 사이에 서로 동일하는 값이 있는지를 확인하고, 담을 빈 리스트 생성
for a in list_a:
    for b in list_b: # list_a와 list_b내부의 값을 순차적으로 매칭, list_a와 list_b의 끝 값까지 무언가를 연산하도록 설정
        if a == b: # list_a와 list_b 내부에 동일한 값이 있으면 find_list에 추가
            find_list.append(a)

print(set(find_list)) # 중복되는 값을 제거하기.


# ^
# set()을 사용하지않고, 원래로직을 개선해서
# find_list에 중복값이 저장되지않도록 해보기

list_a = random.sample(range(10),7) # sample(,) 형식 ^
list_b = [1,5,4,1,2,1,5,1,7,1]

find_list = [] # list_a와 list_b 사이에 서로 동일하는 값이 있는지를 확인하고, 담을 빈 리스트 생성
for a in list_a:
    for b in list_b: # list_a와 list_b내부의 값을 순차적으로 매칭, list_a와 list_b의 끝 값까지 무언가를 연산하도록 설정
        if a == b: # list_a와 list_b 내부에 동일한 값이 있으면 find_list에 추가
            find_list.append(a)