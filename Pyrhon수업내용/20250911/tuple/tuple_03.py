# 튜플 VS 리스트는 서로 변경이 가능하다.
# 튜플 -> 리스트, 리스트 -> 튜플

list_a = [1,2,3]
tuple_a = (10,20,30)

tuple(list_a) # -> 원본 list_a가 수정이 되는 게 아니라, 그 값이 반환되는 형태
print(type(tuple(list_a)))
print(tuple(list_a))
print()
print(type(list_a))
print(list_a)

print()
# list_a 를 완전히 튜플로 바꾸고 싶은 경우
list_a = tuple(list_a)
print(type(list_a))
print(list_a)
# 이렇게 사용한다.

list(tuple_a) # -> 이것도 마찬가지,