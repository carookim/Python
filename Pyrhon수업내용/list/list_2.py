list_a = [1,2,"문자열",True,False]
print(list_a[2][2])

# 원본을 복사
# start_index  : end_index
print(list_a[:]) 
print(list_a[:3])
print(list_a[3:])
print(list_a[-2:])
print(list_a[-1:1]) # ^ 시작인덱스 와 끝인덱스 번호가 순서가 맞지않게 적혀지면 []가 출력이 된다.

# start_index  : end_index : step
print(list_a[::2])

#역순으로 출력
print(list_a[::-1])

# 리스트의 길이를 넘은 인덱스 번호를 입력, 그 해당되는 값에 접근하려고 하면 에러가 뜬다.

# 리스트를 선언합니다.
list_a = [1,2,3]
list_b = [4,5,6]

last_name = "홍"
first_name = "길동"

# 기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()
# "list_a + list_b = " + list_a + list_b
# 이 경우 에러가 뜨는데 그 이유는 다른 자료형끼리 연산을 시키려고 해서다.
# 그래서 다른 문자열이 포함된,자료형 끼리 합하기 위해서는 형변환을 하거나 , 를 사용한다? ^ f-string을 사용한다.

# f-string 사용 해서 기본연산
print(f"list_a + list_b = {list_a + list_b}")
print(f"list_a * 2 = {list_a * 2}")

# 함수
print("함수길이 구하기")
print(len(list_b))
print(len(list_a * 3))
print(len(list_a + list_b))

print(f'last_name + first_name = {last_name + first_name}')
print(f'last_name * 2 = {last_name * 2}')

list_c = [ 
    list_a[0] + list_b[0],
    list_a[1] + list_b[1],
    list_a[2] + list_b[2]
]
# [1, 2, 3, 4, 5, 6]
# [2, 3, 4, 5, 6, 7]
# 이런 식의 리스트를 위 아래로 1+2, 2+3, ...이런식으로
# 바로 합치는 기능은 파이썬에 없지만 넘파이에서 사용이 가능하다.