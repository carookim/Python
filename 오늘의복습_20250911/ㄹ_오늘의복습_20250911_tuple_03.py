# tuple_03 )
#  튜플 형변환
# 튜플 VS 리스트는 서로 변경이 가능하다.
# 튜플 -> 리스트, 리스트 -> 튜플

# 튜플, 리스트 생성
list_a = [1,2,3]
tuple_a = (10,20,30)

print('# 튜플 -> 리스트')
tuple(list_a)
# 이렇게 사용한다.

print(type(tuple(list_a)))
print(tuple(list_a))
print()

print(type(list_a))
print(list_a)
print()
# list_a 자체가 튜플로 변환된것은 아니다.
# -> 원본 list_a가 튜플로 바뀌게 하는 게 아니라, 그 값이 형변환되어 반환되는 형태이다.

print('# list_a 를 완전히 튜플로 바꾸고 싶은 경우')
print(type(list_a))
print()

list_a = tuple(list_a)
# 이렇게 사용한다.

print(type(list_a))
print(list_a)
print()

print('# 리스트 -> 튜플')
list(tuple_a)
# 이렇게 사용한다.

print(type(list(tuple_a)))
print(list(tuple_a))
print()

print(type(tuple_a))
print(tuple_a)
print()
# tuple_a 자체가 리스트로 변환된것은 아니다.
# -> 원본 tuple_a가 리스트으로 바뀌게 하는 게 아니라, 그 값이 형변환되어 반환되는 형태이다.

# 여기서 새로 배운 함수 : 형변환 함수
# tuple()
# list()