# 한번 정리 : 딕셔너리, 튜플, 리스트, 집합 등 4가지 기본 컨테이너들의 메소드/ 함수 기능 정리해보기

# 값을 제거하는 메소드

# 리스트 list
# .remove(value) : 리스트에서 value와 일치하는 "첫 번째 요소"만 삭제
list_a = [1,2,3,2,5] # list 정의
print(list_a.remove(2)) # 반환값 없음
print(list_a) # 인덱스 번호상 앞에 있는 값 2 제거 확인

# .pop(index) : 리스트에서 index에 해당하는 값 삭제 및 삭제된 값 반환
list_a = [1,2,3,4,5] # list 정의
deleted_value = list_a.pop(2)
print(deleted_value) # 반환값 존재
print(list_a) # list_a에서 인덱스 번호상 2에 위치한 값 3 제거 확인

# del list[index]
list_a = [1,2,3,4,5] # list 정의
# deleted_value = del list_a[4] # del 문이라 변수에 대입할수도 변수로 대입할수도 없다. 삭제하는 기능만 가진 함수
del list_a[4] # 반환값 없음 ^ 표현식과 문
print(list_a) # list_a에서 인덱스 번호상 4에 위치한 값 5 제거 확인

# clear()
list_a = [1,2,3,4,5] # list 정의
list_a.clear

# set
# .remove(value)
# .pop()
# .discard(value) ^ 원소 삭제, 삭제할 원소 없어도 에러 없음
# clear()

# dict
# del dict[key]
# .pop(key) ^0 key 제거후 value 반환
# .popitem() ^0 임의의 key-value 삭제 후 반환 ^^ Python 3.7+ 기준으로 삽입 순서에서 마지막 item 제거
# setdefault(key, default) ^
# clear()

# tuple
# immutable, 수정 불가

# 값을 추가하는 함수
# list
# .append(value)
# .insert(value,index)
# .extend(iterable)

# tuple
# immutable, 수정 불가


# set
# .add(value) ^0 단일값 추가 ^
# .update(iterable) ^0 여러값 추가 ^

# dict
# .update(iterable)
# dict[key] = value

# 컨테이너에 대한 정보를 구하는 함수
# list
# len(list)
# value in list ^
# max(list) / min(list) ^

# list.count(value) ^
# list.index(value[, start[, end]]) ^^
# sum(list)

# tuple

# set
# len(set)
# value in set ^
# max(set) / min(set) ^

# .issubset(other) / .issuperset(other) / .isdisjoint(other) ^0 set 전용^^

# dict
# len(dict)
# key in dict ^

# .keys() ^
# .values() ^
# .items() ^
# .get(key[, default]) ^^

# https://chatgpt.com/s/t_68c2d4bf82e48191b91012505d2dba09