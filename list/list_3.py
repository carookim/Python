# 리스트를 선언 합니다.
list_a = [1,2,3]
print(list_a)

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print('-' * 30)

# 리스트 중간에 요소 추가하기
print("리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

# append 사용
# append는 결과값을 반환하지 않는다.
list_a = [1,2,3]
list_a.append([4,5,6])
print(list_a)

# extend 사용
# extend는 결과값을 반환하지 않는다.
list_a = [1,2,3]
list_a.extend([4,5,6])
print(list_a)

# extend 없이 연산 (1)
list_a = [1,2,3]
print(list_a + [4,5,6])

# extend 없이 연산 (2)
list_a = [1,2,3]
print(list_a)
list_a += [4,5,6]
print(list_a)

list_a = [0,1,2,3,4,5]
print('# 리스트의 요소하나 제거하기')

# 제거 방법[1] - del
del list_a[1]
print(f'del lsit_a[1] : {list_a}')

list_a = [0,1,2,3,4,5]
# 제거 방법[2] - pop
list_a.pop(1)
print(f'list_a.pop(1) : {list_a}')

# 랜덤 라이브러리 가져오기
import random
# import 파이썬 프로그램에서 기존에 잘 사용하지않는 기능(라이브러리 기능)을 가져오는 명령어

# 랜덤 라이브러리 중에서 sample 함수 호출
random_numbers = random.sample(range(100),5)
# print(random_numbers)

# random.sample(범위, 갯수)
# random이라는 상자를 가져와서 거기서 sampe이라는 도구를 꺼내서
# 0부터 99까지의 임의의 값을 추출해서 5개가 들어있는 리스트를 생성한다.
# 이 리스트를 어떻게 출력하고 그 리스트 명은 뭐길래? 아 변수로 생성해야되는 구나

# 0 ~ 10 사이중에서 랜덤하게 한개 추출
random_int = random.randint(0,10)

random_numbers.append(random_int)
# 이 상태에서 in, not in을 사용하더라도 True, False 값이 항상 동일하지않게 값이 나온다.
# 0부터 99까지 임의로 5개를 추출한 리스트 마지막에 0 ~ 10 중에서 랜덤하게 한개를 추출한 값을 추가한다.

# 50이 있는지
print(50 in random_numbers)
print(random_numbers)

print('-' * 30)

# 삭제
print(random_numbers)
del random_numbers[0]
print(random_numbers)
# del 내가 삭제한 데이터가 뭔지 알 수 없다. 그냥 삭제한다.
# del은 앞에 다가 기재, 삭제한 값이 뭔지 알 수 없다. 그래서 따로 그 인덱싱하여 삭제할 값을 미리 출력을 하든 다른 처리가 필요하다.
print(random_numbers)
removed_number = random_numbers.pop(0)
print(random_numbers)
print(removed_number)
# 지정된 값이 첫번째로 일치하는 값을 삭제하고 반환한다.
# pop 내가 삭제한 데이터가 뭔지 알 수 있다. 그걸 빼서 가져다 오듯이, 삭제를 하면서 그 값을 가져온다.
# pop은 .뒤에 기재, 삭제한 값을 알 수 있다. 그래서 삭제한값을 확인해볼수도 있다.

# clear

# remove