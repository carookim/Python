# ! 리스트 컴프리헨션 여러가지 사례 복습할때 해보기

# 1)  if 구문을 사용하면서 한줄로 정리하기
print([ i for i in range(5) if i % 2== 0])
# 'if i % 2== 0' 이 조건에 해당할때에만 list에 포함한다.

# 2) enumerate와 if 구문을 활용하여 한줄로 정리하기
list_1 = [1,2,3,1,2,3,5,4,8]
# 값 2에 해당하는 인덱스를 찾아서 리스트로 반환
# [1,4]

print([ idx for idx,value in enumerate(list_1) if value == 2]) # for i in range() 여기서 i에 두가지 변수가 들어간 경우 ^

# 3) if, else 구문 한줄로 정리하기
age = 20
if age >= 18:
    result = '성인'
else:
    result = '미성년'

# 이걸 한줄로 표현
result = '성인' if age >= 18 else '미성년' # 삼합연산자

# 4)
list_1 = [1,2,1,5,3,2,1,54]
# git