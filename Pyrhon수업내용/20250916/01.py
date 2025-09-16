# 파일 위치 : 01.py

# 1] 리스트 컴프리 핸션

# [ 표현식 for 변수 in 반복가능객체 ]
# 표현식 : 리스트에 들어갈 값. 여기서는 i

# for 변수 in 반복가능객체 : 반복할 범위나 컬렉션. 여기서는 range(1, 11)

# 이렇게 쓰면 반복문 한 줄로 리스트를 만들 수 있음


import random
# 1)
# total = []
# for i in range(1,11):
#     total.append(i)

print( [ i for i in range(1,11) ] )

# 2)
total = []
for i in range(5):
    total.append(random.randint(1,10))
import random
print([random.randint(1,10) for i in range(5)])