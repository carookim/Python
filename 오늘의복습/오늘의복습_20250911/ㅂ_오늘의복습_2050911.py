# 파일 위치 : set_01.py

# 5] 집합 형변환(1)

# 리스트 -> 집합

# 집합, 리스트 생성
set_a = {1,2,3,1,2,3,1}
list_a = [100, 500, 10, 500, 100, 50, 500, 10]

print('# 집합 -> 셋')
set(list_a)
print(type(set(list_a)))
print(set(list_a))
print()

print(type(list_a))
print(list_a)
print()
# list_a 자체가 셋으로 변환된것은 아니다.
# -> 원본 list_a가 셋으로 바뀌게 하는 게 아니라, 그 값이 형변환되어 반환되는 형태이다.
# type()가 출력되는 거라,type()에서 형변환된 값이 출력되는 것

# ^
# iterable(반복 가능한 객체)
# iterable = for문에서 하나씩 꺼낼 수 있는 자료형
# 대표적인 iterable → 문자열, 리스트, 튜플, 딕셔너리, 집합
# 대표적인 not iterable → 숫자형(정수,실수), bool, None

# 여기서 새로 배운 함수 : 형변환 함수
# set()