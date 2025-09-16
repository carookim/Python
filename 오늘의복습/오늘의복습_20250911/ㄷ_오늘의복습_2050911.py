# 파일 위치 : tuple_02.py

# 2] 튜플

# tuple 튜플, 불변객체
# 불변, 반복가능, 인덱스 O, 순서 O
tuple_1 = (1,1,2,3,4) # () 소괄호
print(tuple_1[0])
# 튜플은 담긴 값을 수정불가하다. -> 읽고 값을 보관하는 기능을 한다.

# 튜플.메소드(1)
# 튜플.count(x) 특정 값 x가 몇 번 나타나는지의 값을 반환한다.
tuple_1.count(1)
# 이렇게 사용한다.

print(tuple_1.count(1))

# 튜플.메소드(2)
# 튜플.index(x), 튜플 내의 값 x의 인덱스 값을 반환한다.
tuple_1.index(4)
# 이렇게 사용한다.

print(tuple_1.index(4))

# 시퀀스형(list, tuple , str)에 위 메소드 .count()와 .index() 를 제공한다.

# 여기서 새로 배운 메소드 : 시퀀스형에서 제공하는 메소드
# .count()
# .index()